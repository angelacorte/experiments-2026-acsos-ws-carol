@file:Suppress("UndocumentedPublicFunction")

package it.unibo.collektive.alchemist.device

import it.unibo.alchemist.collektive.device.CollektiveDevice
import it.unibo.alchemist.model.Position
import it.unibo.alchemist.model.molecules.SimpleMolecule
import it.unibo.alchemist.model.positions.Euclidean2DPosition
import it.unibo.collektive.alchemist.device.sensors.EnvironmentVariables
import it.unibo.collektive.alchemist.device.sensors.LocationSensor
import it.unibo.collektive.model.Device
import it.unibo.collektive.model.Obstacle
import it.unibo.collektive.model.SpeedControl2D
import it.unibo.collektive.model.Target
import it.unibo.collektive.model.Vector2D

/**
 * Relocates the current node to [newPosition] within the environment.
 */
context(device: CollektiveDevice<Euclidean2DPosition>)
fun moveNodeToPosition(newPosition: Vector2D) {
    val envPos: Position<Euclidean2DPosition> = device.environment.makePosition(newPosition.x, newPosition.y)
    device.environment.moveNodeToPosition(device.node, envPos as Euclidean2DPosition)
}

/**
 * Relocates a node identified by [nodeID] to [newPosition].
 */
context(device: CollektiveDevice<Euclidean2DPosition>)
fun moveNodeToPosition(nodeID: Int, newPosition: Vector2D) {
    val envPos: Position<Euclidean2DPosition> = device.environment.makePosition(newPosition.x, newPosition.y)
    val node = device.environment.nodes.find { it.id == nodeID }
    if (node != null) {
        device.environment.moveNodeToPosition(node, envPos as Euclidean2DPosition)
    } else {
        error("Could not find a node with ID $nodeID")
    }
}

/**
 * Fetches a target by [targetId] from the current location sensor context.
 */
context(position: LocationSensor)
fun getTarget(targetId: Number): Target =
    position.targetsPosition().find { it.id == targetId } ?: error("Target $targetId not found.")

/**
 * Builds a [Device] view for the current device state using environment variables.
 */
context(position: LocationSensor, env: EnvironmentVariables)
fun getRobot(): Device = position.coordinates().let {
    val velocity = env.getOrDefault("Control", SpeedControl2D(0.0, 0.0))
    Device(it.x, it.y, env["SafeMargin"], velocity, env["MaxSpeed"])
}

/**
 * Returns the first obstacle in the environment, failing fast if none is present.
 */
context(device: CollektiveDevice<*>)
fun getObstacle(): Obstacle {
    val obstacle =
        device.environment.nodes.firstOrNull { it.contains(SimpleMolecule("Obstacle")) }
            ?: error("Currently, there are no obstacles in the environment")
    val obstaclePos = device.environment.getPosition(obstacle).coordinates
    val radius = obstacle.getConcentration(SimpleMolecule("SafeRadius")) as Double
    val margin = obstacle.getConcentration(SimpleMolecule("SafeMargin")) as Double
    return Obstacle(obstaclePos[0], obstaclePos[1], radius, margin)
}

/**
 * Applies the computed control [velocity][control] to the robot by moving its node inside the environment.
 *
 * Under ZOH dynamics the displacement is ∆t · u:  p_{k+1} = p_k + ∆t · u_k.
 */
context(locationSensor: LocationSensor, device: CollektiveDevice<Euclidean2DPosition>)
fun applyControl(control: SpeedControl2D, deltaTime: Double): Device {
    device["DeltaTime"] = deltaTime
    device["Control"] = control
    device["Velocity"] = control
    return getRobot().copy(control = control)
}
