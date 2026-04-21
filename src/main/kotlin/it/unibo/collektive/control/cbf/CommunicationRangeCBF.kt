package it.unibo.collektive.control.cbf

import com.gurobi.gurobi.GRB
import com.gurobi.gurobi.GRBLinExpr
import com.gurobi.gurobi.GRBModel
import it.unibo.collektive.mathutils.minus
import it.unibo.collektive.mathutils.squaredNorm
import it.unibo.collektive.mathutils.toDoubleArray
import it.unibo.collektive.model.Device
import it.unibo.collektive.solver.gurobi.Constraint
import it.unibo.collektive.solver.gurobi.GRBVector
import it.unibo.collektive.solver.gurobi.QpSettings
import kotlin.math.max
import kotlin.math.pow

/**
 * Communication-range barrier: keeps two robots within [range] of each other.
 *
 * Robustified discrete-time CBF under ZOH dynamics (installed once, updated every iteration):
 * ```
 * −2(p_i − p_j)ᵀ(u_i − u_j) + slack ≥ −(η/Δt)·h_com + 4Δt·u_max²
 * ```
 * where `h_com = R² − ‖p_i − p_j‖²`.
 *
 * Both the LHS coefficients and the RHS change with robot positions and Δt.
 * [GRBModel.chgCoeff] updates them without structural changes.
 *
 * @property range      maximum allowed distance between the two robots
 * @property eta        decay-rate parameter
 * @property slackWeight penalty for the soft version; `null` → hard constraint
 */
class CommunicationRangeCBF(
    private val range: Double,
    override val eta: Double = 0.5,
    override val slackWeight: Double? = null,
) : CBF() {

    override val name: String = "communication_range_CBF"
    override fun GRBModel.installCBF(selfDecision: GRBVector, otherDecision: GRBVector?): Constraint {
        checkNotNull(otherDecision) { "CommunicationRangeCBF requires the neighbor decision vector" }
        val slack = slackWeight?.let {
            addVar(0.0, GRB.INFINITY, 0.0, GRB.CONTINUOUS, "slack_$name")
        }
        val lhs = GRBLinExpr().apply {
            repeat(selfDecision.dimensions) { i ->
                addTerm(0.0, selfDecision[i])
                addTerm(0.0, otherDecision[i])
            }
            slack?.let { addTerm(1.0, it) }
        }
        val constraint = addConstr(lhs, GRB.GREATER_EQUAL, 0.0, name)

        return object : Constraint {
            override val slack = slack
            override val slackWeight = this@CommunicationRangeCBF.slackWeight
            override fun update(
                model: GRBModel,
                self: Device,
                otherDevice: Device?,
                settings: QpSettings,
                deltaTime: Double,
            ) {
                checkNotNull(otherDevice) {
                    "CommunicationRangeCBF.update: otherRobot must not be null"
                }
                val distance = (self.position - otherDevice.position).toDoubleArray()
                val h = range.pow(2) - distance.squaredNorm()
                val maxSpeed = max(self.maxSpeed, otherDevice.maxSpeed)
                val rhs = -(eta / deltaTime) * h + 4 * deltaTime * maxSpeed.pow(2)
//                val rhs = -(eta / deltaTime) * h + 4 * deltaTime * (self.maxSpeed + otherRobot.maxSpeed).pow(2)
                constraint.set(GRB.DoubleAttr.RHS, rhs)
                for (i in distance.indices) {
                    model.chgCoeff(constraint, selfDecision[i], -2.0 * distance[i])
                    model.chgCoeff(constraint, otherDecision[i], 2.0 * distance[i])
                }
            }
        }
    }
}
