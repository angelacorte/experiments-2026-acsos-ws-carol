package it.unibo.collektive.control.cbf

import com.gurobi.gurobi.GRB
import com.gurobi.gurobi.GRBLinExpr
import com.gurobi.gurobi.GRBModel
import it.unibo.collektive.control.ControlFunction
import it.unibo.collektive.mathutils.minus
import it.unibo.collektive.mathutils.squaredNorm
import it.unibo.collektive.mathutils.toDoubleArray
import it.unibo.collektive.model.Device
import it.unibo.collektive.model.Obstacle
import it.unibo.collektive.solver.gurobi.Constraint
import it.unibo.collektive.solver.gurobi.GRBVector
import it.unibo.collektive.solver.gurobi.QpSettings
import kotlin.math.pow

/**
 * Static obstacle-avoidance barrier under ZOH dynamics.
 *
 * Discrete-time CBF constraint (installed once, updated every iteration):
 * ```
 * 2(p_i − p_o)ᵀ u_i + slack ≥ −(η/Δt) · h_obs
 * ```
 * where `h_obs = ‖p_i − p_o‖² − (r_o + d_o)²`.
 *
 * The obstacle and robot positions may change across iterations, so the current obstacle is
 * retrieved through [obstacleProvider] during every update and the numerical values are refreshed
 * via [GRBModel.chgCoeff].
 *
 * @property obstacleProvider supplies the current obstacle to avoid
 * @property eta        decay-rate parameter
 * @property slackWeight penalty for the soft version; `null` → hard constraint
 */
class ObstacleAvoidanceCBF(
    override val eta: Double = 0.5,
    override val slackWeight: Double? = null,
    private var obstacleProvider: () -> Obstacle,
) : CBF() {

    override val name: String = "obstacle_avoidance_CBF"

    override fun syncFrom(other: ControlFunction) {
        if (other is ObstacleAvoidanceCBF) {
            obstacleProvider = other.obstacleProvider
        }
    }

    override fun GRBModel.installCBF(selfDecision: GRBVector, otherDecision: GRBVector?): Constraint {
        val slack = slackWeight?.let {
            addVar(0.0, GRB.INFINITY, 0.0, GRB.CONTINUOUS, "slack_$name")
        }
        val lhs = GRBLinExpr().apply {
            repeat(selfDecision.dimensions) { i -> addTerm(0.0, selfDecision[i]) }
            slack?.let { addTerm(1.0, it) }
        }
        val constr = addConstr(lhs, GRB.GREATER_EQUAL, 0.0, name)

        return object : Constraint {
            override val slack = slack
            override val slackWeight = this@ObstacleAvoidanceCBF.slackWeight
            override fun update(
                model: GRBModel,
                self: Device,
                otherDevice: Device?,
                settings: QpSettings,
                deltaTime: Double,
            ) {
                val obstacle = this@ObstacleAvoidanceCBF.obstacleProvider()
                val distance = (self.position - obstacle).toDoubleArray()
                val h = distance.squaredNorm() - (obstacle.radius + obstacle.margin).pow(2)
                val rhs = -(eta / deltaTime) * h
                constr.set(GRB.DoubleAttr.RHS, rhs)
                for (i in distance.indices) {
                    model.chgCoeff(constr, selfDecision[i], 2.0 * distance[i])
                }
            }
        }
    }
}
