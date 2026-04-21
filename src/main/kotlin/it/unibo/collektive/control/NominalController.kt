package it.unibo.collektive.control

import it.unibo.collektive.mathutils.nominal
import it.unibo.collektive.model.Device
import it.unibo.collektive.model.SpeedControl2D
import it.unibo.collektive.model.Target

/**
 * Computes the nominal control for a robot, representing its desired
 * behavior in the absence of constraints (e.g., obstacles or neighbors).
 */
fun interface NominalController {
    /**
     * Computes the desired nominal speed for the given [device].
     *
     * @param device the robot for which the nominal control is calculated.
     * @return the computed [SpeedControl2D] representing the unconstrained intended velocity.
     */
    fun compute(device: Device): SpeedControl2D
}

/**
 * A simple proportional controller driving the robot toward a static target.
 *
 * The computed nominal control follows the proportional law:
 * `u_i^nom = - gain * (p_i - p_g)`
 * where `p_i` is the robot's position and `p_g` is the target's position.
 *
 * @property target the [Target] the robot should navigate towards.
 * @property gain the proportional gain of the controller (default is 0.5).
 */
class GoToTargetNominal(private val gain: Double = 0.5, private val targetProvider: () -> Target) : NominalController {
    override fun compute(device: Device): SpeedControl2D = device.position.nominal(targetProvider().position, gain)
}
