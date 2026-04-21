package it.unibo.collektive.solver.gurobi

import com.gurobi.gurobi.GRB
import com.gurobi.gurobi.GRBModel
import com.gurobi.gurobi.GRBQuadExpr
import com.gurobi.gurobi.GRBVar
import it.unibo.collektive.admm.LocalDualUpdate
import it.unibo.collektive.admm.SuggestedControl
import it.unibo.collektive.control.cbf.CBF
import it.unibo.collektive.mathutils.plus
import it.unibo.collektive.mathutils.toDoubleArray
import it.unibo.collektive.model.Device
import it.unibo.collektive.model.SpeedControl2D

/**
 * Reusable Gurobi model for the pairwise QP solved on a shared edge during ADMM.
 */
class PairwiseQP private constructor(
    private val model: GRBModel,
    private val slack: GRBVar,
    private val zi: GRBVector,
    private val zj: GRBVector,
    private val constraints: List<Constraint>,
) {

    /**
     * Releases the underlying Gurobi model resources.
     */
    fun dispose() = model.dispose()

    /**
     * Updates and solves the pairwise edge model for the current local and neighbor states.
     *
     * @param device current local device state.
     * @param other current neighbor device state.
     * @param incidentDuals dual variables associated with the shared edge.
     * @param settings numerical settings shared by the solver.
     * @param deltaTime control horizon expressed in seconds.
     * @return the consensus controls suggested for both endpoints.
     */
    fun updateAndSolve(
        device: Device,
        other: Device,
        incidentDuals: LocalDualUpdate,
        settings: QpSettings,
        deltaTime: Double,
    ): SuggestedControl {
        val robotArray = device.control.toDoubleArray()
        val otherArray = other.control.toDoubleArray()
        for (i in zi.variables.indices) {
            zi[i].set(GRB.DoubleAttr.LB, -device.maxSpeed)
            zi[i].set(GRB.DoubleAttr.UB, device.maxSpeed)
            zi[i].set(GRB.DoubleAttr.Start, robotArray[i]) // warm start
            zj[i].set(GRB.DoubleAttr.LB, -other.maxSpeed)
            zj[i].set(GRB.DoubleAttr.UB, other.maxSpeed)
            zj[i].set(GRB.DoubleAttr.Start, otherArray[i]) // warm start
        }
        constraints.forEach { constraint -> constraint.update(model, device, other, settings, deltaTime) }
        model.setObjective(buildObjective(device, other, incidentDuals, settings), GRB.MINIMIZE)
        model.update()
        model.optimize()
        return extractSolution(device, other)
    }

    private fun buildObjective(
        device: Device,
        other: Device,
        incidentDuals: LocalDualUpdate,
        settings: QpSettings,
    ): GRBQuadExpr = GRBQuadExpr().apply {
        val rho = settings.rhoADMM / 2.0
        // (ρ/2)‖z_i − (u_i + y_i)‖²  +  (ρ/2)‖z_j − (u_j + y_j)‖²
        addRhoNorm2Sq(zi, (device.control + incidentDuals.yi).toDoubleArray(), rho)
        addRhoNorm2Sq(zj, (other.control + incidentDuals.yj).toDoubleArray(), rho)
        constraints.forEach { constr ->
            constr.slack?.let { slackConstraint ->
                constr.slackWeight?.let { slackWeight ->
                    addTerm(slackWeight, slackConstraint, slackConstraint)
                }
            }
        }
        addTerm(settings.rhoSlack, slack, slack)
    }

    private fun extractSolution(device: Device, other: Device): SuggestedControl {
        val status = model.get(GRB.IntAttr.Status)
        if (status == GRB.INFEASIBLE) {
            model.writeIIS("commonModel.ilp")
            for (c in model.constrs) {
                if (c.get(GRB.IntAttr.IISConstr) == 1) {
                    println("Pairwise IIS constraint: ${c.get(GRB.StringAttr.ConstrName)}")
                }
            }
        }
        if (status == GRB.INF_OR_UNBD) {
            model.set(GRB.IntParam.DualReductions, 0)
            model.reset()
            model.optimize()
        }
        return when {
            model.get(GRB.IntAttr.SolCount) > 0 -> SuggestedControl(
                SpeedControl2D(zi[0].get(GRB.DoubleAttr.X), zi[1].get(GRB.DoubleAttr.X)),
                SpeedControl2D(zj[0].get(GRB.DoubleAttr.X), zj[1].get(GRB.DoubleAttr.X)),
            )
            else -> {
                println("Pairwise QP: no solution found (status $status), returning current controls.")
                SuggestedControl(device.control, other.control)
            }
        }
    }

    /**
     * Factory methods for creating a fully installed pairwise QP model.
     */
    companion object {

        /**
         * Builds a pairwise QP model with all requested edge constraints already installed.
         *
         * @param model Gurobi model to populate.
         * @param device local device used to size the first decision vector.
         * @param other neighbor device used to size the second decision vector.
         * @param pairwiseCBFs pairwise barrier functions to install on the model.
         * @return the reusable pairwise QP wrapper.
         */
        fun create(model: GRBModel, device: Device, other: Device, pairwiseCBFs: List<CBF>): PairwiseQP {
            val slack = model.addVar(0.0, GRB.INFINITY, 0.0, GRB.CONTINUOUS, "slack_pairwiseQP")
            val zi = model.addVecVar(device.position.dimension, -device.maxSpeed, device.maxSpeed, "z_ij^i")
            val zj = model.addVecVar(other.position.dimension, -other.maxSpeed, other.maxSpeed, "z_ij^j")
            val constrs = mutableListOf<Constraint>()
            pairwiseCBFs.forEach { cbf -> constrs += cbf.install(model, zi, zj) }
            model.update()
            return PairwiseQP(
                model = model,
                slack,
                zi = zi,
                zj = zj,
                constraints = constrs,
            )
        }
    }
}
