@file:Suppress("MagicNumber")

package it.unibo.collektive.entrypoints

import it.unibo.alchemist.collektive.device.CollektiveDevice
import it.unibo.alchemist.model.positions.Euclidean2DPosition
import it.unibo.collektive.admm.admmEntrypoint
import it.unibo.collektive.aggregate.api.Aggregate
import it.unibo.collektive.alchemist.device.getObstacle
import it.unibo.collektive.alchemist.device.getRobot
import it.unibo.collektive.alchemist.device.getTarget
import it.unibo.collektive.alchemist.device.sensors.LocationSensor
import it.unibo.collektive.alchemist.device.sensors.TimeSensor
import it.unibo.collektive.control.GoToTargetNominal
import it.unibo.collektive.control.cbf.CollisionAvoidanceCBF
import it.unibo.collektive.control.cbf.MaxSpeedCBF
import it.unibo.collektive.control.cbf.ObstacleAvoidanceCBF
import it.unibo.collektive.control.clf.GoToTargetCLF
import it.unibo.collektive.mathutils.toDoubleArray
import it.unibo.collektive.solver.Solver

/**
 * Multiple Targets simulation entrypoint.
 */
fun Aggregate<Int>.multipleTargetEntrypoint(
    position: LocationSensor,
    timeSensor: TimeSensor,
    device: CollektiveDevice<Euclidean2DPosition>,
    solver: Solver,
) = context(position, device, timeSensor, solver) {
    val robot = getRobot()
    admmEntrypoint(
        device["ControlPeriodMS"] as? Double ?: 100.0,
        robot,
        localCLF = listOf(GoToTargetCLF { getTarget(device["TargetID"] as Number) }),
        uNominal = GoToTargetNominal { getTarget(device["TargetID"] as Number) }.compute(robot).toDoubleArray(),
        localCBF = listOf(ObstacleAvoidanceCBF { getObstacle() }, MaxSpeedCBF()),
        pairwiseCBF = listOf(CollisionAvoidanceCBF(0.8)),
    )
}
