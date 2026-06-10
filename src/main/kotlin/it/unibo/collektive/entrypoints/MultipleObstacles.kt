@file:Suppress("MagicNumber")

package it.unibo.collektive.entrypoints

import it.unibo.alchemist.collektive.device.CollektiveDevice
import it.unibo.alchemist.model.positions.Euclidean2DPosition
import it.unibo.collektive.admm.admmEntrypoint
import it.unibo.collektive.aggregate.api.Aggregate
import it.unibo.collektive.alchemist.device.getObstacle
import it.unibo.collektive.alchemist.device.getObstacles
import it.unibo.collektive.alchemist.device.getRobot
import it.unibo.collektive.alchemist.device.getTarget
import it.unibo.collektive.alchemist.device.sensors.LocationSensor
import it.unibo.collektive.alchemist.device.sensors.TimeSensor
import it.unibo.collektive.control.GoToTargetNominal
import it.unibo.collektive.control.cbf.CollisionAvoidanceCBF
import it.unibo.collektive.control.cbf.CommunicationRangeCBF
import it.unibo.collektive.control.cbf.MaxSpeedCBF
import it.unibo.collektive.control.cbf.ObstacleAvoidanceCBF
import it.unibo.collektive.control.clf.GoToTargetCLF
import it.unibo.collektive.mathutils.toDoubleArray
import it.unibo.collektive.solver.Solver

/**
 * Main aggregate entrypoint: runs distributed ADMM to compute a safe control and applies it when converged.
 */
fun Aggregate<Int>.multipleObstaclesEntrypoint(
    position: LocationSensor,
    timeSensor: TimeSensor,
    device: CollektiveDevice<Euclidean2DPosition>,
    solver: Solver,
) = context(position, device, timeSensor, solver) {
    val myTarget = device["TargetID"] as Number
    val robot = getRobot()
    val communicationDistance: Double = device["CommunicationDistance"]
    val obstacles = getObstacles()
    val obstaclesCBF = obstacles.map { ObstacleAvoidanceCBF { it } }
    admmEntrypoint(
        device["ControlPeriodMS"] as? Double ?: 100.0,
        robot,
        uNominal = GoToTargetNominal { getTarget(myTarget) }.compute(robot).toDoubleArray(),
        localCLF = listOf(GoToTargetCLF { getTarget(myTarget) }),
        localCBF = obstaclesCBF + MaxSpeedCBF(),
        pairwiseCBF = listOf(
            CollisionAvoidanceCBF(0.8),
            CommunicationRangeCBF(communicationDistance, 0.3, slackWeight = 0.5),
        ),
    )
}
