package it.unibo.collektive.alchemist.device

import it.unibo.collektive.admm.Tolerance
import it.unibo.collektive.solver.gurobi.QpSettings

/**
 * Centralized tuning parameters for the ADMM QP solver.
 *
 * Controls: [rhoSlack] (default slack weight), [rhoADMM] (ADMM penalty),
 * [rhoResidual] (residual balancing), [tolerance] (primal and dual residual thresholds),
 * and [logEnabled] (enable solver logging).
 *
 * Per-iteration values such as the simulation delta-time are intentionally kept out of this class
 * so a cached solver can safely reuse the same settings for the whole environment.
 */
data class SimulationQpSettings(
    override val constraintPrefix: String,
    override val logEnabled: Boolean,
    override val rhoADMM: Double,
    override val rhoResidual: Double,
    override val rhoSlack: Double,
    override val tolerance: Tolerance,
) : QpSettings
