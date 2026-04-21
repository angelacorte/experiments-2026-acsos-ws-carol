package it.unibo.collektive.solver.gurobi

import it.unibo.collektive.admm.Tolerance

/**
 * Numerical and runtime configuration shared by the quadratic programs used in the ADMM solver.
 */
interface QpSettings {
    /**
     * Prefix used when generating Gurobi constraint names.
     */
    val constraintPrefix: String

    /**
     * Whether Gurobi logging should be enabled.
     */
    val logEnabled: Boolean

    /**
     * ADMM penalty parameter used in the consensus terms of the objective.
     */
    val rhoADMM: Double

    /**
     * Scaling factor used when evaluating the dual residual.
     */
    val rhoResidual: Double

    /**
     * Default penalty applied to slack variables.
     */
    val rhoSlack: Double

    /**
     * Residual thresholds used to evaluate convergence and confidence.
     */
    val tolerance: Tolerance
}
