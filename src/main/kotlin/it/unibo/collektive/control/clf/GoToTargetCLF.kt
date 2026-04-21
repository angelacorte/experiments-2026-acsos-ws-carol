package it.unibo.collektive.control.clf

import com.gurobi.gurobi.GRB
import com.gurobi.gurobi.GRBLinExpr
import com.gurobi.gurobi.GRBModel
import it.unibo.collektive.control.ControlFunction
import it.unibo.collektive.mathutils.minus
import it.unibo.collektive.mathutils.squaredNorm
import it.unibo.collektive.mathutils.toDoubleArray
import it.unibo.collektive.model.Device
import it.unibo.collektive.model.Target
import it.unibo.collektive.solver.gurobi.Constraint
import it.unibo.collektive.solver.gurobi.GRBVector
import it.unibo.collektive.solver.gurobi.QpSettings
import kotlin.math.pow

/**
 * Discrete-time CLF constraint for goal-reaching under ZOH dynamics.
 *
 * Installed constraint (built once):
 * ```
 * 2Δt·(p_i − p_g)ᵀ·u − slack  ≤  −λ·‖p_i − p_g‖² − Δt²·u_max²
 * ```
 *
 * Both the LHS coefficients `2Δt·(p_i − p_g)[k]` and the RHS change every iteration as the robot
 * moves. The current target is retrieved through [targetProvider] on every update so the cached
 * solver model can react to target motion at runtime.
 *
 * The slack variable is mandatory for CLF feasibility and is provided by the enclosing local QP
 * as the shared node slack `ω_i`.
 *
 * @property targetProvider  supplies the current navigation goal
 * @property convergenceRate Lyapunov decrease rate λ
 * @property slackWeight     objective penalty for the slack variable (default 1.0)
 */
class GoToTargetCLF(
    override val convergenceRate: Double = 1.0,
    override val slackWeight: Double? = 1.0,
    private var targetProvider: () -> Target,
) : CLF() {

    override val name: String = "go_to_target"

    override fun syncFrom(other: ControlFunction) {
        if (other is GoToTargetCLF) {
            targetProvider = other.targetProvider
        }
    }

    override fun GRBModel.installCLF(selfDecision: GRBVector): Constraint {
        val slack = addVar(0.0, GRB.INFINITY, 0.0, GRB.CONTINUOUS, "slack_$name")
        val lhs = GRBLinExpr().apply {
            repeat(selfDecision.dimensions) { i -> addTerm(0.0, selfDecision[i]) }
            addTerm(-1.0, slack)
        }
        val constr = addConstr(lhs, GRB.LESS_EQUAL, 0.0, "${name}_CLF")

        return object : Constraint {
            override val slack = slack
            override val slackWeight = this@GoToTargetCLF.slackWeight

            override fun update(
                model: GRBModel,
                self: Device,
                otherDevice: Device?,
                settings: QpSettings,
                deltaTime: Double,
            ) {
                val target = this@GoToTargetCLF.targetProvider()
                val distance = (self.position - target.position).toDoubleArray()
                val rhs = -convergenceRate * distance.squaredNorm() - deltaTime.pow(2) * self.maxSpeed.pow(2)
                constr.set(GRB.DoubleAttr.RHS, rhs)
                for (i in distance.indices) {
                    model.chgCoeff(constr, selfDecision[i], 2.0 * deltaTime * distance[i])
                }
            }
        }
    }
}
