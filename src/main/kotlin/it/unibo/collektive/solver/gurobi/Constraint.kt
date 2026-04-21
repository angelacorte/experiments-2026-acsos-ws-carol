package it.unibo.collektive.solver.gurobi

import com.gurobi.gurobi.GRBModel
import com.gurobi.gurobi.GRBVar
import it.unibo.collektive.control.ControlFunction
import it.unibo.collektive.model.Device

/**
 * A handle to variables and constraints that have been structurally installed into a [GRBModel] **exactly once**.
 *
 * After [ControlFunction.install] returns this handle, the model topology is frozen.
 * Every ADMM iteration must only call [update] to refresh numerical parameters (RHS, linear coefficients,
 * variable bounds) and then call [GRBModel.update] once before [GRBModel.optimize].
 *
 * Gurobi's [GRBModel.addVar] / [GRBModel.addConstr] are comparatively expensive: they allocate
 * internal data structures and require a full model rebuild on every [GRBModel.update] call.
 * [GRBModel.chgCoeff] and attribute setters (RHS, bounds) are cheap in-place mutations that do
 * **not** trigger a structural rebuild, so they are the right tool for per-iteration updates.
 */
interface Constraint {

    /**
     * The slack decision variable introduced for this constraint,
     * or `null` if the constraint is enforced as hard (no slack).
     */
    val slack: GRBVar?

    /**
     * The objective penalty weight applied to [slack].
     * `null` means this constraint does not contribute its own slack penalty.
     */
    val slackWeight: Double?

    /**
     * Refreshes the numerical values used by the installed constraint without changing model topology.
     *
     * @param model owning Gurobi model.
     * @param self current state of the local device.
     * @param otherDevice current state of the neighbor device, when this is a pairwise constraint.
     * @param settings numerical settings shared by the active QP.
     * @param deltaTime control horizon expressed in seconds.
     */
    fun update(model: GRBModel, self: Device, otherDevice: Device? = null, settings: QpSettings, deltaTime: Double)
}
