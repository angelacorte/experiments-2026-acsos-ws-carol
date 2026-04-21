package it.unibo.collektive.control.clf

import com.gurobi.gurobi.GRBModel
import it.unibo.collektive.control.ControlFunction
import it.unibo.collektive.solver.gurobi.Constraint
import it.unibo.collektive.solver.gurobi.GRBVector

/**
 * Base class for Control Lyapunov Functions.
 *
 * Subclasses implement [GRBModel.installCLF], which is called **once** per model to add the
 * Lyapunov decrease constraint.  Subsequent per-iteration parameter refreshes happen through the
 * returned [Constraint.update].
 *
 * Note that CLF instances may carry dynamic goal information (e.g. a target position that moves).
 * The [Constraint.update] method receives the **current** CLF instance as its `cf` parameter
 * so that updated goal positions can be read without rebuilding the model structure.
 */
abstract class CLF : ControlFunction {

    override val name: String get() = "CLF"

    /** Rate at which the Lyapunov function is forced to decrease toward zero. */
    abstract val convergenceRate: Double

    /**
     * Adds the CLF decrease constraint to `this` model exactly once.
     *
     * Add the slack variable and constraint here with placeholder zero coefficients for
     * position-dependent terms.  Capture all GRB handles in the returned [Constraint].
     */
    abstract fun GRBModel.installCLF(selfDecision: GRBVector): Constraint

    final override fun install(model: GRBModel, selfDecision: GRBVector, otherDecision: GRBVector?): Constraint =
        model.installCLF(selfDecision)
}
