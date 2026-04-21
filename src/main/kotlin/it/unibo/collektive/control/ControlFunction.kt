package it.unibo.collektive.control

import com.gurobi.gurobi.GRBExpr
import com.gurobi.gurobi.GRBLinExpr
import com.gurobi.gurobi.GRBModel
import com.gurobi.gurobi.GRBQuadExpr
import com.gurobi.gurobi.GRBVar
import it.unibo.collektive.solver.gurobi.Constraint
import it.unibo.collektive.solver.gurobi.GRBVector
import it.unibo.collektive.solver.gurobi.QpSettings

/**
 * A control function (CLF or CBF) that integrates into an ADMM QP via a two-phase protocol:
 *
 * [install] adds all decision variables and constraints to a fresh [GRBModel] and returns an
 * [Constraint] that owns the resulting GRB handles.  After this call the model
 * **topology** is fixed: no further `addVar` / `addConstr` calls will be made for this function.
 *
 * [Constraint.update] rewrites only the *numerical* parameters — RHS values and linear
 * coefficients — via [GRBModel.chgCoeff] and attribute setters.  A single [GRBModel.update] call
 * is issued by the owning template after all constraints have been refreshed.
 */
interface ControlFunction {

    /** Unique identifier used for Gurobi constraint naming. */
    val name: String

    /**
     * Penalty weight applied to the slack variable in the QP objective, or `null` when this control
     * function should not introduce/use its own slack.
     */
    val slackWeight: Double?

    /**
     * Installs this control function into [model] by creating all of its variables and constraints once.
     *
     * @param model target Gurobi model.
     * @param selfDecision decision vector for the local endpoint.
     * It corresponds to the local control variable `u` in single-device QPs and to `z_i` in pairwise QPs.
     * @param otherDecision decision vector for the neighbor endpoint, when the function is pairwise.
     * It is `null` for single-device QPs and corresponds to `z_j` in pairwise QPs.
     * @return a handle that can refresh the installed numerical coefficients at runtime.
     */
    fun install(model: GRBModel, selfDecision: GRBVector, otherDecision: GRBVector?): Constraint

    /**
     * Refreshes runtime data from another instance with the same installed model topology.
     *
     * Default implementation is a no-op; dynamic control functions can override it to swap
     * providers or other mutable parameters without rebuilding the model.
     */
    fun syncFrom(other: ControlFunction) = Unit

    /**
     * Legacy helper for objective slack penalties.
     * The active QP builders currently manage slack penalties directly.
     */
    fun addSlackToObjective(objective: GRBExpr, slack: GRBVar, settings: QpSettings) {
        val weight = slackWeight ?: settings.rhoSlack
        when (objective) {
            is GRBLinExpr -> objective.addTerm(weight, slack)
            is GRBQuadExpr -> objective.addTerm(weight, slack)
            else -> error("Cannot add slack to objective of type ${objective::class.simpleName}")
        }
    }
}
