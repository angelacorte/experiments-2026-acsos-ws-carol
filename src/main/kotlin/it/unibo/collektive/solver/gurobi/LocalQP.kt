package it.unibo.collektive.solver.gurobi

import com.gurobi.gurobi.GRB
import com.gurobi.gurobi.GRBModel
import com.gurobi.gurobi.GRBQuadExpr
import com.gurobi.gurobi.GRBVar
import it.unibo.collektive.admm.DualParams
import it.unibo.collektive.control.cbf.CBF
import it.unibo.collektive.control.clf.CLF
import it.unibo.collektive.mathutils.minus
import it.unibo.collektive.mathutils.toDoubleArray
import it.unibo.collektive.model.Device
import it.unibo.collektive.model.SpeedControl2D

/**
 * Reusable Gurobi model for the single-device QP solved during each ADMM iteration.
 */
class LocalQP private constructor(
    private val model: GRBModel,
    private val u: GRBVector,
    private val slack: GRBVar,
    private val localCLFs: List<CLF>,
    private val localCBFs: List<CBF>,
    private val constraints: List<Constraint>,
) {

    /**
     * Releases the underlying Gurobi model resources.
     */
    fun dispose() = model.dispose()

    /**
     * Synchronizes the already-installed control functions with the latest runtime instances.
     *
     * The number and ordering of functions must match the topology used when the model was created.
     */
    fun syncControlFunctions(localCLFs: List<CLF>, localCBFs: List<CBF>) {
        require(this.localCLFs.size == localCLFs.size) {
            "Expected ${this.localCLFs.size} local CLFs, got ${localCLFs.size}"
        }
        require(this.localCBFs.size == localCBFs.size) {
            "Expected ${this.localCBFs.size} local CBFs, got ${localCBFs.size}"
        }
        this.localCLFs.zip(localCLFs).forEach { (installed, current) -> installed.syncFrom(current) }
        this.localCBFs.zip(localCBFs).forEach { (installed, current) -> installed.syncFrom(current) }
    }

    /**
     * Updates variable bounds, refreshes constraint coefficients, solves the QP, and returns the new control.
     *
     * @param device current local device state.
     * @param uNominal nominal control used by the quadratic objective.
     * @param duals per-neighbor ADMM state used to build the consensus penalty.
     * @param settings numerical settings shared by the solver.
     * @param deltaTime control horizon expressed in seconds.
     * @return the control selected by the optimizer, or the previous control if no solution is found.
     */
    fun <ID : Comparable<ID>> updateAndSolve(
        device: Device,
        uNominal: DoubleArray,
        duals: Map<ID, DualParams>,
        settings: QpSettings,
        deltaTime: Double,
    ): SpeedControl2D {
        for (i in u.variables.indices) {
            u[i].set(GRB.DoubleAttr.LB, -device.maxSpeed)
            u[i].set(GRB.DoubleAttr.UB, device.maxSpeed)
            u[i].set(GRB.DoubleAttr.Start, device.control.toDoubleArray()[i]) // warm start
        }
        constraints.forEach { constraint ->
            constraint.update(model, device, settings = settings, deltaTime = deltaTime)
        }
        model.setObjective(buildObjective(uNominal, duals, settings), GRB.MINIMIZE)
        model.update()
        model.optimize()
        return extractSolution(device)
    }

    private fun buildObjective( // todo this should be taken from outside, can be different by different simulations
        uNominal: DoubleArray,
        duals: Map<*, DualParams>,
        settings: QpSettings,
    ): GRBQuadExpr = GRBQuadExpr().apply {
        addRhoNorm2Sq(u, uNominal)
        constraints.forEach { constr ->
            constr.slack?.let { slackConstraint ->
                constr.slackWeight?.let { slackWeight ->
                    addTerm(slackWeight, slackConstraint, slackConstraint)
                }
            }
        }
        addTerm(settings.rhoSlack, slack, slack)
        duals.forEach { (_, value) ->
            val suggested = value.suggestedControl.zi.toDoubleArray()
            val residual = value.localDualUpdate.yi.toDoubleArray()
            addRhoNorm2Sq(u, suggested - residual, settings.rhoADMM / 2.0)
        }
    }

    private fun extractSolution(device: Device): SpeedControl2D {
        val status = model.get(GRB.IntAttr.Status)
        if (status == GRB.INFEASIBLE) {
            model.writeIIS("localModel.ilp")
            for (constr in model.constrs) {
                if (constr.get(GRB.IntAttr.IISConstr) == 1) {
                    println("Local IIS constraint: ${constr.get(GRB.StringAttr.ConstrName)}")
                }
            }
        }
        if (status == GRB.INF_OR_UNBD) {
            model.set(GRB.IntParam.DualReductions, 0)
            model.reset()
            model.optimize()
        }
        return when {
            model.get(
                GRB.IntAttr.SolCount,
            ) > 0 -> SpeedControl2D(u[0].get(GRB.DoubleAttr.X), u[1].get(GRB.DoubleAttr.X))
            else -> {
                println("Local QP: no solution found (status $status), returning previous control.")
                device.control
            }
        }
    }

    /**
     * Factory methods for creating a fully installed local QP model.
     */
    companion object {
        /**
         * Builds a local QP model with all requested control functions already installed.
         *
         * @param model Gurobi model to populate.
         * @param device device used to size the control vector and bounds.
         * @param localCLFs local CLF constraints to install.
         * @param localCBFs local CBF constraints to install.
         * @return the reusable local QP wrapper.
         */
        fun create(model: GRBModel, device: Device, localCLFs: List<CLF>, localCBFs: List<CBF>): LocalQP {
            val u = model.addVecVar(device.position.dimension, -device.maxSpeed, device.maxSpeed, "u")
            val slack = model.addVar(0.0, GRB.INFINITY, 0.0, GRB.CONTINUOUS, "slack_localQP")
            val installed = mutableListOf<Constraint>()
            localCLFs.forEach { clf -> installed += clf.install(model, u, null) }
            localCBFs.forEach { cbf -> installed += cbf.install(model, u, null) }
            model.update()
            return LocalQP(
                model = model,
                u = u,
                slack,
                localCLFs = localCLFs,
                localCBFs = localCBFs,
                constraints = installed,
            )
        }
    }
}
