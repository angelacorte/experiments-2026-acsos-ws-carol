package it.unibo.collektive.admm

import it.unibo.alchemist.collektive.device.CollektiveDevice
import it.unibo.alchemist.model.positions.Euclidean2DPosition
import it.unibo.collektive.aggregate.api.Aggregate
import it.unibo.collektive.aggregate.api.exchanging
import it.unibo.collektive.aggregate.api.sharing
import it.unibo.collektive.aggregate.toMap
import it.unibo.collektive.alchemist.device.applyControl
import it.unibo.collektive.alchemist.device.sensors.LocationSensor
import it.unibo.collektive.alchemist.device.sensors.TimeSensor
import it.unibo.collektive.control.cbf.CBF
import it.unibo.collektive.control.clf.CLF
import it.unibo.collektive.mathutils.minus
import it.unibo.collektive.mathutils.norm
import it.unibo.collektive.mathutils.plus
import it.unibo.collektive.model.Device
import it.unibo.collektive.model.SpeedControl2D
import it.unibo.collektive.solver.Solver
import it.unibo.collektive.solver.gurobi.QpSettings
import it.unibo.collektive.stdlib.spreading.gossipMax
import it.unibo.collektive.stdlib.time.sharedTimeLeftTo
import kotlin.math.max
import kotlin.time.Duration
import kotlin.time.Duration.Companion.ZERO
import kotlin.time.Duration.Companion.milliseconds
import kotlin.time.DurationUnit
import kotlin.time.ExperimentalTime

/**
 * Aggregate entrypoint: runs the distributed ADMM control loop and applies the resulting velocity.
 */
@OptIn(ExperimentalTime::class)
context(
    collektiveDevice: CollektiveDevice<Euclidean2DPosition>,
    locationSensor: LocationSensor,
    solver: Solver,
    timeSensor: TimeSensor,
)
fun Aggregate<Int>.admmEntrypoint(
    controlPeriod: Double,
    device: Device,
    uNominal: DoubleArray,
    localCLF: List<CLF>,
    localCBF: List<CBF>,
    pairwiseCBF: List<CBF>,
) {
    val timeLeft = sharedTimeLeftTo(timeSensor.getTimeAsInstant(), controlPeriod.milliseconds).also {
        collektiveDevice["TimeLeft"] = it
    }
    val controlPeriodSeconds = Duration.convert(controlPeriod, DurationUnit.MILLISECONDS, DurationUnit.SECONDS)
    // device snapshots
    evolve(device) { previous ->
        solver.setupLocalModel(previous, localCLF, localCBF)
        val control = admm(previous, uNominal, controlPeriodSeconds, pairwiseCBF)
        when {
            timeLeft <= ZERO -> applyControl(control, controlPeriodSeconds)
            else -> previous
        }
    }
}

context(solver: Solver)
internal inline fun <reified ID : Comparable<ID>> Aggregate<ID>.admm(
    device: Device,
    uNominal: DoubleArray,
    controlPeriod: Double,
    pairwiseCBF: List<CBF>,
): SpeedControl2D = evolving(ControlAndDuals(device.control)) { previous ->
    val previousDuals = previous.duals.filterNot { localId == it.key }
    val control: SpeedControl2D = solver.updateAndSolveLocal(
        device.copy(control = previous.control),
        uNominal,
        previousDuals,
        controlPeriod,
    )
    val deviceUpdated = device.copy(control = control)
    val updatedDuals: Map<ID, DualParams> = exchanging(EdgeInfo(deviceUpdated)) { field ->
        field.map { (neighborID: ID, neighborData: EdgeInfo) ->
            val neighborInfo = neighborData.device
            val previousLocalUpdate: LocalDualUpdate =
                previousDuals[neighborID]?.localDualUpdate ?: LocalDualUpdate()
            when {
                isOwnerOf(neighborID) -> {
                    if (!solver.isPairwiseModelAvailable) {
                        solver.setupPairwiseModel(
                            deviceUpdated,
                            neighborInfo,
                            pairwiseCBF,
                        )
                    }
                    val (zi, zj) = solver.updateAndSolvePairwise(
                        deviceUpdated,
                        neighborInfo,
                        previousLocalUpdate,
                        controlPeriod,
                    )
                    val updatedEdgeState = DualParams(
                        SuggestedControl(zi, zj),
                        LocalDualUpdate(
                            previousLocalUpdate.yi + deviceUpdated.control - zi,
                            previousLocalUpdate.yj + neighborInfo.control - zj,
                        ),
                    )
                    EdgeInfo(deviceUpdated, updatedEdgeState.suggestedControl, updatedEdgeState.localDualUpdate)
                }
                else -> {
                    val ownerEdgeState = DualParams(
                        neighborData.suggestedControl,
                        neighborData.localDualUpdate,
                    ).swap()
                    EdgeInfo(deviceUpdated, ownerEdgeState.suggestedControl, ownerEdgeState.localDualUpdate)
                }
            }
        }.yielding {
            neighbors.toMap().mapValues { (_, edgeData) ->
                DualParams(edgeData.suggestedControl, edgeData.localDualUpdate)
            }
        }
    }
    val controlAndDuals = ControlAndDuals(deviceUpdated.control, updatedDuals)
    val previousSuggested = previousDuals.mapValues { it.value.suggestedControl }
    val (primalResidual, dualResidual) = residualUpdate(solver.settings, controlAndDuals, previousSuggested)
    val confidence = confidence(primalResidual, dualResidual, solver.settings.tolerance)
    val scaledControl = SpeedControl2D(
        controlAndDuals.control.x * confidence,
        controlAndDuals.control.y * confidence,
    )
    controlAndDuals.yielding { scaledControl }
}

/**
 * Executes one ADMM iteration using the provided dual variables and returns the updated local state.
 *
 * The local QP is solved first to refresh the node control, then the pairwise QPs are evaluated
 * against each neighbor to produce the consensus suggestions and dual updates associated with each edge.
 *
 * @param device current state of the local device.
 * @param uNominal nominal control used as the reference objective for the local QP.
 * @param duals current per-neighbor dual state.
 * @param deltaTime control horizon expressed in seconds.
 * @param solver solver instance used for both local and pairwise QPs.
 * @param pairwiseCBF pairwise barrier functions that constrain shared edges.
 * @return the updated control together with the refreshed dual parameters.
 */
context(solver: Solver)
fun <ID : Comparable<ID>> Aggregate<ID>.coreADMM(
    device: Device,
    uNominal: DoubleArray,
    duals: Map<ID, DualParams>,
    deltaTime: Double,
    pairwiseCBF: List<CBF>,
): ControlAndDuals<ID> {
    val control: SpeedControl2D = solver.updateAndSolveLocal(device, uNominal, duals, deltaTime)
    val deviceUpdated = device.copy(control = control)
    return sharing(deviceUpdated) { controls ->
        val commons: Map<ID, DualParams> = controls.neighbors.toMap()
            .filterNot { it.key == localId }
            .mapValues { (neighborId, neighbor) ->
                val incidentDuals = duals[neighborId]?.localDualUpdate ?: LocalDualUpdate()
                if (!solver.isPairwiseModelAvailable) solver.setupPairwiseModel(device, neighbor, pairwiseCBF)
                val (zi, zj) = solver.updateAndSolvePairwise(deviceUpdated, neighbor, incidentDuals, deltaTime)
                val newIncidentDuals = LocalDualUpdate(
                    incidentDuals.yi + control - zi, // y_ij^i,t+1
                    incidentDuals.yj + neighbor.control - zj, // y_ij^j,t+1
                )
                DualParams(SuggestedControl(zi, zj), newIncidentDuals)
            }
        deviceUpdated.yielding { ControlAndDuals(control, commons) }
    }
}

/**
 * Returns `true` when the current device is the canonical owner of the edge shared with [otherID].
 *
 * Ownership is assigned to the endpoint with the smallest identifier so that exactly one device
 * performs the pairwise optimization for each edge.
 */
fun <ID : Comparable<ID>> Aggregate<ID>.isOwnerOf(otherID: ID): Boolean =
    localId != otherID && minOf(localId, otherID) == localId

private inline fun <reified ID : Comparable<ID>> Aggregate<ID>.residualUpdate(
    settings: QpSettings,
    output: ControlAndDuals<ID>,
    previousSuggested: Map<ID, SuggestedControl>,
): Residuals {
    val currentSuggested = output.duals.filterNot { it.key == localId }.mapValues { it.value.suggestedControl }
    val primalResidualLocal = currentSuggested.maxOfOrNull { (_, v) -> (output.control - v.zi).norm() } ?: 0.0
    val primalResidualGlobal = gossipMax(primalResidualLocal)
    val dualResidualLocal = currentSuggested.maxOfOrNull { (id, v) ->
        val prev = previousSuggested[id] ?: SuggestedControl()
        settings.rhoResidual * (v.zi - prev.zi).norm()
    } ?: 0.0
    val dualResidualGlobal = gossipMax(dualResidualLocal)
    return Residuals(primalResidualGlobal, dualResidualGlobal)
}

private fun confidence(primalResidual: Double, dualResidual: Double, tolerance: Tolerance): Double {
    val error = max(primalResidual / tolerance.primal, dualResidual / tolerance.dual)
    return if (error <= 1.0) 1.0 else 1.0 / error
}

internal data class EdgeInfo(
    val device: Device,
    val suggestedControl: SuggestedControl = SuggestedControl(),
    val localDualUpdate: LocalDualUpdate = LocalDualUpdate(),
)
