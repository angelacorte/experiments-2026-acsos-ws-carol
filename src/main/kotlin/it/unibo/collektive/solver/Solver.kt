package it.unibo.collektive.solver

import it.unibo.collektive.admm.DualParams
import it.unibo.collektive.admm.LocalDualUpdate
import it.unibo.collektive.admm.SuggestedControl
import it.unibo.collektive.control.cbf.CBF
import it.unibo.collektive.control.clf.CLF
import it.unibo.collektive.model.Device
import it.unibo.collektive.model.SpeedControl2D
import it.unibo.collektive.solver.gurobi.QpSettings

/**
 * Contract for optimization backends used to solve local and pairwise ADMM subproblems.
 *
 * A `Solver` implementation is responsible for:
 * - creating and maintaining optimization models,
 * - updating model coefficients from the current system state,
 * - solving both local and edge-coupled QPs,
 * - returning controls in the domain model format.
 *
 * Typical usage sequence:
 * 1. Configure local and pairwise models through setup methods.
 * 2. At each control step, call update-and-solve methods with fresh state and ADMM duals.
 */
interface Solver {

    /**
     * Static and numeric settings used by the underlying QP backend.
     */
    val settings: QpSettings

    /**
     * Whether the local-device QP has already been created.
     */
    val isLocalModelAvailable: Boolean

    /**
     * Whether the pairwise-edge QP has already been created.
     */
    val isPairwiseModelAvailable: Boolean

    /**
     * Creates the local-device QP if needed, or synchronizes the installed control functions otherwise.
     *
     * @param device device used to size and initialize the optimization variables.
     * @param localCLFs local control Lyapunov functions enforced by the model.
     * @param localCBFs local control barrier functions enforced by the model.
     */
    fun setupLocalModel(device: Device, localCLFs: List<CLF>, localCBFs: List<CBF>)

    /**
     * Creates the pairwise QP used to negotiate controls on an edge, if it is not available yet.
     *
     * @param device local device involved in the pairwise optimization.
     * @param otherDevice neighbor device involved in the pairwise optimization.
     * @param pairwiseCBFs pairwise barrier functions enforced on the shared edge.
     */
    fun setupPairwiseModel(device: Device, otherDevice: Device, pairwiseCBFs: List<CBF>)

    /**
     * Updates and solves the local-device QP for the current ADMM iteration.
     *
     * @param device current local device state.
     * @param uNominal nominal control used as the tracking objective.
     * @param duals per-neighbor ADMM dual state.
     * @param deltaTime control horizon expressed in seconds.
     * @return the optimized local control.
     */
    fun <ID : Comparable<ID>> updateAndSolveLocal(
        device: Device,
        uNominal: DoubleArray,
        duals: Map<ID, DualParams>,
        deltaTime: Double,
    ): SpeedControl2D

    /**
     * Updates and solves the pairwise QP associated with a shared edge.
     *
     * @param device local device state.
     * @param otherDevice neighbor device state.
     * @param duals dual variables currently associated with the edge.
     * @param deltaTime control horizon expressed in seconds.
     * @return the consensus controls suggested for the local and neighbor endpoints.
     */
    fun updateAndSolvePairwise(
        device: Device,
        otherDevice: Device,
        duals: LocalDualUpdate,
        deltaTime: Double,
    ): SuggestedControl
}
