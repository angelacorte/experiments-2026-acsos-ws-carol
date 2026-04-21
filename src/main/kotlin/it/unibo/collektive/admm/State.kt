package it.unibo.collektive.admm

import it.unibo.collektive.model.SpeedControl2D
import it.unibo.collektive.model.Vector2D
import it.unibo.collektive.model.initVector2D
import it.unibo.collektive.model.zeroSpeed

/**
 * Container for ADMM iteration information.
 * @param iteration Current iteration number.
 * @param admmOutput Control and duals for the current iteration.
 */
data class Infos<ID : Comparable<ID>>(val iteration: Int, val admmOutput: ControlAndDuals<ID>)

/**
 * Output control decision for a node.
 * @param shouldApply Whether the control should be applied.
 * @param control The control to apply.
 */
data class OutputControl(val shouldApply: Boolean, val control: SpeedControl2D)

/**
 * Control decision and dual map for the current node.
 * @property [control] optimal control for the node.
 * @property [duals] per-neighbor dual parameters.
 */
data class ControlAndDuals<ID : Comparable<ID>>(
    val control: SpeedControl2D,
    val duals: Map<ID, DualParams> = emptyMap(),
)

/**
 * Local dual bundle for a neighbor edge.
 * @property [suggestedControl] consensus controls for the edge.
 * @property [localDualUpdate] associated dual variables.
 */
data class DualParams(
    val suggestedControl: SuggestedControl = SuggestedControl(),
    val localDualUpdate: LocalDualUpdate = LocalDualUpdate(),
) {
    override fun toString(): String =
        "DualParams(suggestedControl=$suggestedControl, \n incidentDuals=$localDualUpdate)"

    /**
     * Swaps the local and neighbor perspectives stored in this edge state.
     */
    fun swap(): DualParams = DualParams(suggestedControl.swap(), localDualUpdate.swap())
}

/**
 * Dual variables associated to an edge (stored from the local and neighbor perspective).
 * @property [yi] local dual variable.
 * @property [yj] neighbor dual variable.
 */
data class LocalDualUpdate(val yi: Vector2D = initVector2D(), val yj: Vector2D = initVector2D()) {
    override fun toString(): String = "IncidentDuals(yi=(${yi.x}, ${yi.y}), yj=(${yj.x}, ${yj.y})"

    /**
     * Swaps the endpoint-associated dual variables.
     */
    fun swap(): LocalDualUpdate = LocalDualUpdate(yj, yi)
}

/**
 * Suggested consensus controls for the two edge endpoints.
 * @property [zi] control suggested for the local node.
 * @property [zj] control suggested for the neighbor node.
 */
data class SuggestedControl(val zi: SpeedControl2D = zeroSpeed(), val zj: SpeedControl2D = zeroSpeed()) {
    override fun toString(): String = "SuggestedControl(zi=(${zi.x}, ${zi.y}), zj=(${zj.x}, ${zj.y})"

    /**
     * Swaps the consensus controls assigned to the two edge endpoints.
     */
    fun swap(): SuggestedControl = SuggestedControl(zj, zi)
}

/**
 * Primal/dual residuals for stopping criteria.
 * @property [primalResidual] maximum primal residual.
 * @property [dualResidual] maximum dual residual.
 */
data class Residuals(val primalResidual: Double, val dualResidual: Double)

/**
 * Absolute and relative tolerances used to stop ADMM iterations.
 * @property [primal] primal residual threshold.
 * @property [dual] dual residual threshold.
 */
data class Tolerance(val primal: Double, val dual: Double)
