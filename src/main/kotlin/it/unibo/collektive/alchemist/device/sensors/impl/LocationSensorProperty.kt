package it.unibo.collektive.alchemist.device.sensors.impl

import it.unibo.alchemist.model.Environment
import it.unibo.alchemist.model.Node
import it.unibo.alchemist.model.NodeProperty
import it.unibo.alchemist.model.Position
import it.unibo.alchemist.model.molecules.SimpleMolecule
import it.unibo.collektive.alchemist.device.sensors.LocationSensor
import it.unibo.collektive.model.Coordinate
import it.unibo.collektive.model.Target

/**
 * An implementation of a location sensor property for nodes in an Alchemist environment.
 *
 * @param T the concentration type managed by the node
 * @param P the position type used in the environment
 * @property environment the simulation environment
 * @property node the node associated with this sensor property
 * @property random an instance of a random number generator for simulating measurement noise
 * @property stdDev the standard deviation for Gaussian noise added to target positions
 */
class LocationSensorProperty<T : Any, P : Position<P>>(
    private val environment: Environment<T, P>,
    override val node: Node<T>,
) : LocationSensor,
    NodeProperty<T> {

    override fun cloneOnNewNode(node: Node<T>): NodeProperty<T> = LocationSensorProperty(environment, node)

    override fun coordinates(): Coordinate {
        val position = environment.getPosition(node).coordinates
        return Coordinate(position[0], position[1])
    }

    override fun surroundings(): List<Coordinate> = environment.getNeighborhood(node).map { node ->
        environment.getPosition(node).coordinates.let { Coordinate(it[0], it[1]) }
    }

    override fun targetsPosition(): List<Target> = environment.nodes
        .filter { node ->
            node.contains(SimpleMolecule("Target"))
        }.map { target ->
            (target.getConcentration(SimpleMolecule("Target")) as Number) to environment.getPosition(target)
        }.map { (id, position) ->
            Target(position.coordinates[0], position.coordinates[1], id)
        }
}
