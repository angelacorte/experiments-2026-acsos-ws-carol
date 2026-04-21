package it.unibo.collektive.control.cbf

import com.gurobi.gurobi.GRB
import com.gurobi.gurobi.GRBModel
import it.unibo.collektive.model.Device
import it.unibo.collektive.solver.gurobi.Constraint
import it.unibo.collektive.solver.gurobi.GRBVector
import it.unibo.collektive.solver.gurobi.QpSettings
import it.unibo.collektive.solver.gurobi.toQuadExpr
import kotlin.math.pow

/**
 * Maximum-speed constraint enforced as a quadratic barrier.
 *
 * Constraint (installed once):
 * ```
 * ‖u_i‖² ≤ u_max²
 * ```
 *
 * The quadratic structure `‖u‖²` is immutable after install.  Only the RHS `u_max²` may change if
 * the robot's maximum speed is adjusted between iterations; this is updated via the [GRBQConstr]
 * RHS attribute setter — no structural changes are needed.
 *
 * @property eta unused (kept for interface compatibility with [CBF])
 * @property slackWeight always `null`; slack on a quadratic norm constraint requires a quadratic
 *  addition to the LHS which is not supported after [GRBModel.addQConstr].
 *  Use variable bounds on the decision vector as an alternative soft limit if needed.
 */
class MaxSpeedCBF(override val eta: Double = 1.0, override val slackWeight: Double? = null) : CBF() {

    override val name: String = "max_speed"

    override fun GRBModel.installCBF(selfDecision: GRBVector, otherDecision: GRBVector?): Constraint {
        val lhsExpr = selfDecision.toQuadExpr()
        val qConstr = addQConstr(lhsExpr, GRB.LESS_EQUAL, 0.0, "u_norm_sq")
        return object : Constraint {
            override val slack = null
            override val slackWeight = this@MaxSpeedCBF.slackWeight
            override fun update(
                model: GRBModel,
                self: Device,
                otherDevice: Device?,
                settings: QpSettings,
                deltaTime: Double,
            ) {
                qConstr.set(GRB.DoubleAttr.QCRHS, self.maxSpeed.pow(2))
            }
        }
    }
}
