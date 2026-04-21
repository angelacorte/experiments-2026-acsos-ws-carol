package it.unibo.alchemist.model.movestrategies.target

import it.unibo.alchemist.model.Environment
import it.unibo.alchemist.model.Node
import it.unibo.alchemist.model.Position
import it.unibo.alchemist.model.Reaction
import it.unibo.alchemist.model.Time
import it.unibo.alchemist.model.molecules.SimpleMolecule
import it.unibo.alchemist.model.movestrategies.SpeedSelectionStrategy
import it.unibo.collektive.model.SpeedControl2D
import kotlin.math.hypot

/**
 * A [SpeedSelectionStrategy] that determines the movement length of a node based on its velocity and time step.
 *
 * This strategy retrieves the node's velocity from the "Velocity" molecule, expecting it to be a [SpeedControl2D].
 * The movement length is computed as the magnitude of the velocity vector multiplied by the time step.
 * The time step is taken from the "DeltaTime" molecule if present, otherwise it is computed as the inverse
 * of the reaction's time distribution rate.
 *
 * @param T the type of the concentrations in the environment
 * @param P the type of position used in the environment
 * @property node the node whose speed and properties are used to determine the movement length
 * @property reaction the reaction associated with the node, used to retrieve the time distribution rate
 */
class SpeedFromMolecule<T, P : Position<P>>(private val node: Node<T>, private val environment: Environment<T, P>) :
    SpeedSelectionStrategy<T, P> {

    /**
     * Last simulation time used to compute the elapsed time for the next movement update.
     */
    var previousTime: Time = Time.ZERO

    override fun getNodeMovementLength(target: P?): Double {
        val speed = node.getConcentration(SimpleMolecule("Velocity")) as? SpeedControl2D ?: return 0.0
        val speedMagnitude = hypot(speed.x, speed.y)
        val current = environment.simulation.time
        val deltaTime = (current - previousTime).toDouble()
        previousTime = current
//        val deltaTime = node.ge/tConcentration(SimpleMolecule("DeltaTime")) as? Double
//            ?: (1.0 / reaction.timeDistribution.rate)
        return speedMagnitude * deltaTime
    }
}
