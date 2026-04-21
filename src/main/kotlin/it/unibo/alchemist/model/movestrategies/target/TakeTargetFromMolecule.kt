package it.unibo.alchemist.model.movestrategies.target

import it.unibo.alchemist.model.Environment
import it.unibo.alchemist.model.Node
import it.unibo.alchemist.model.Position
import it.unibo.alchemist.model.molecules.SimpleMolecule
import it.unibo.alchemist.model.movestrategies.TargetSelectionStrategy
import it.unibo.collektive.model.SpeedControl2D

/**
 * A target selection strategy that computes the next target position for a node
 * based on the presence of a "Robot" molecule and a "Velocity" molecule.
 *
 * If the node contains the "Robot" molecule and has a non-zero velocity (as a [SpeedControl2D]),
 * the target is projected in the direction of the velocity vector, scaled by 1000.
 * Otherwise, the current position is returned as the target.
 *
 * @param T the type of the concentration in the environment
 * @param P the type of position used in the environment
 * @property environment the environment in which the node moves
 * @property node the node whose target is being computed
 */
class TakeTargetFromMolecule<T, P : Position<P>>(
    private val environment: Environment<T, P>,
    private val node: Node<T>,
) : TargetSelectionStrategy<T, P> {

    override fun getTarget(): P? {
        val currentPos = environment.getPosition(node)
        val speed = node.getConcentration(SimpleMolecule("Velocity")) as? SpeedControl2D
        return when {
            node.contains(SimpleMolecule("Robot")) && speed != null && (speed.x != 0.0 || speed.y != 0.0) -> {
                environment.makePosition(
                    currentPos.coordinates[0] + speed.x * 1000.0,
                    currentPos.coordinates[1] + speed.y * 1000.0,
                )
            }
            else -> currentPos
        }
    }
}
