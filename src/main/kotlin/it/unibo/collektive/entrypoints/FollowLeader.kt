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
import it.unibo.collektive.control.cbf.CommunicationRangeCBF
import it.unibo.collektive.control.cbf.MaxSpeedCBF
import it.unibo.collektive.control.cbf.ObstacleAvoidanceCBF
import it.unibo.collektive.control.clf.GoToTargetCLF
import it.unibo.collektive.mathutils.toDoubleArray
import it.unibo.collektive.model.Target
import it.unibo.collektive.solver.Solver
import it.unibo.collektive.stdlib.consensus.boundedElection
import it.unibo.collektive.stdlib.spreading.hopGradientCast

/**
 * Entrypoint for simulation where the leader goes towards a target and other nodes have as target the leader.
 */
fun Aggregate<Int>.followLeaderEntrypoint(
    position: LocationSensor,
    timeSensor: TimeSensor,
    device: CollektiveDevice<Euclidean2DPosition>,
    solver: Solver,
) = context(position, device, timeSensor, solver) {
    val robot = getRobot()
    val communicationDistance: Double = device["CommunicationDistance"]

    val leaderID = boundedElection(strength = localId, bound = communicationDistance.toInt())
    val isLeader = (leaderID == localId).also { device["isLeader"] = it }

    val leaderAsTarget = hopGradientCast(isLeader, robot.position)
        .let { coordinate -> Target(coordinate.x, coordinate.y, leaderID) }

    val targetSelectionStrategy = when {
        isLeader -> getTarget(device["TargetID"] as Number)
        else -> leaderAsTarget
    }

    admmEntrypoint(
        device["ControlPeriodMS"] as? Double ?: 100.0,
        robot,
        uNominal = GoToTargetNominal { targetSelectionStrategy }.compute(robot).toDoubleArray(),
        localCLF = listOf(GoToTargetCLF { targetSelectionStrategy }),
        localCBF = listOf(ObstacleAvoidanceCBF { getObstacle() }, MaxSpeedCBF()),
        pairwiseCBF = listOf(
            CollisionAvoidanceCBF(0.8),
            CommunicationRangeCBF(communicationDistance, 0.3, slackWeight = 0.5),
        ),
    )
}
