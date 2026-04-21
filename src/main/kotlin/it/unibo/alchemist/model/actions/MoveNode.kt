package it.unibo.alchemist.model.actions

import it.unibo.alchemist.model.Action
import it.unibo.alchemist.model.Environment
import it.unibo.alchemist.model.Node
import it.unibo.alchemist.model.Reaction
import it.unibo.alchemist.model.molecules.SimpleMolecule
import it.unibo.alchemist.model.positions.Euclidean2DPosition
import it.unibo.collektive.model.SpeedControl2D
import it.unibo.collektive.model.zeroSpeed

/**
 * Represents a movement action that updates the position of a node within a Euclidean 2D environment.
 * This class defines the motion dynamics, including velocity, boundaries, and trajectory behavior.
 *
 * @param T the concentration type managed by the node
 * @param environment the simulation environment in which the node resides
 * @param node the node under movement
 * @param reaction the reaction associated with this action
 */
class MoveNode<T>(environment: Environment<T, Euclidean2DPosition>, node: Node<T>, private val reaction: Reaction<T>) :
    AbstractMoveNode<T, Euclidean2DPosition>(environment, node, false) {

    override fun getNextPosition(): Euclidean2DPosition {
        val speed = node.getConcentration(speedMolecule) as? SpeedControl2D
            ?: zeroSpeed()
        val dt = node.getConcentration(SimpleMolecule("DeltaTime")) as? Double
            ?: (1.0 / reaction.timeDistribution.rate)
//        node.setConcentration(speedMolecule, zeroSpeed() as T) // todo maybe it's wrong to do it here
        return Euclidean2DPosition(speed.x * dt, speed.y * dt)
    }

    override fun cloneAction(p0: Node<T>, p1: Reaction<T>): Action<T> = MoveNode(environment, node, reaction)

    /**
     * Companion object for Move Node Action.
     */
    companion object {
        /**
         * The molecule representing the velocity vector for the node.
         */
        val speedMolecule = SimpleMolecule("Velocity")
    }
}
