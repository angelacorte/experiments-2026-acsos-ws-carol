package it.unibo.collektive.control.cbf

import com.gurobi.gurobi.GRBModel
import it.unibo.collektive.control.ControlFunction
import it.unibo.collektive.solver.gurobi.Constraint
import it.unibo.collektive.solver.gurobi.GRBVector

/**
 * Base class for Control Barrier Functions.
 *
 * Subclasses implement [GRBModel.installCBF], which is called **once** per model to add the
 * barrier constraint structure.  Subsequent per-iteration parameter refreshes happen through the
 * returned [Constraint.update].
 */
abstract class CBF : ControlFunction {

    override val name: String get() = "CBF"

    /** Decay-rate parameter governing how strictly the barrier is enforced. */
    abstract val eta: Double

    /**
     * Adds the barrier constraint to `this` model exactly once.
     *
     * Add variables and constraints here using placeholder zero coefficients for any term
     * whose value depends on robot positions.  Capture the resulting [GRBConstr]/[GRBQConstr]
     * handles in the returned [Constraint] closure.
     *
     * @see Constraint.update for the per-iteration numerical refresh
     */
    abstract fun GRBModel.installCBF(selfDecision: GRBVector, otherDecision: GRBVector?): Constraint

    final override fun install(model: GRBModel, selfDecision: GRBVector, otherDecision: GRBVector?): Constraint =
        model.installCBF(selfDecision, otherDecision)
}
