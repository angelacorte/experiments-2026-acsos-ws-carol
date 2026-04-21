package it.unibo.alchemist.model.implementations.reactions

import it.unibo.alchemist.model.Action
import it.unibo.alchemist.model.Actionable
import it.unibo.alchemist.model.Condition
import it.unibo.alchemist.model.Dependency
import it.unibo.alchemist.model.Environment
import it.unibo.alchemist.model.GlobalReaction
import it.unibo.alchemist.model.Node
import it.unibo.alchemist.model.Position
import it.unibo.alchemist.model.Time
import it.unibo.alchemist.model.TimeDistribution
import it.unibo.alchemist.model.molecules.SimpleMolecule
import it.unibo.alchemist.model.positions.Euclidean2DPosition
import org.danilopianini.util.ListSet
import org.danilopianini.util.ListSets

/**
 * Represents a movement action that updates the position of a node within a Euclidean 2D environment.
 * This class defines the motion dynamics, including velocity, boundaries, and trajectory behavior.
 *
 * @param T the concentration type managed by the node
 * @param environment the simulation environment in which the node resides
 * @param distribution the time distribution of this reaction
 * @param xDest the destination of the node along the x-axis
 * @param yDest the destination of the node along the y-axis
 * @param targetID the ID of the target to move
 */
class MoveTarget<T>(
    val environment: Environment<T, Euclidean2DPosition>,
    val distribution: TimeDistribution<T>,
    val xDest: Double,
    val yDest: Double,
    val targetID: Int,
) : GlobalReaction<T> {

    private var executed = false

    override var actions: List<Action<T>> = mutableListOf()
        set(value) {
            field = listOf(*value.toTypedArray())
        }

    override var conditions: List<Condition<T>> = mutableListOf()
        set(value) {
            field = listOf(*value.toTypedArray())
        }

    override val rate: Double
        get() = distribution.getRate()

    override val tau: Time
        get() = distribution.nextOccurence

    override val inboundDependencies: ListSet<out Dependency> = ListSets.emptyListSet()

    override val outboundDependencies: ListSet<out Dependency> = ListSets.emptyListSet()

    override val timeDistribution: TimeDistribution<T> = distribution

    override fun execute() {
        if (!executed) {
            executed = true
            moveTargetTo(targetID, xDest, yDest)
            distribution.update(timeDistribution.nextOccurence, true, rate, environment)
        }
    }

    override fun canExecute(): Boolean = true

    override fun initializationComplete(atTime: Time, environment: Environment<T, *>) = Unit

    override fun update(currentTime: Time, hasBeenExecuted: Boolean, environment: Environment<T, *>) = Unit

    override fun compareTo(other: Actionable<T>): Int = tau.compareTo(other.tau)

    private fun moveTargetTo(targetId: Number, vararg to: Number) {
        val targetNode = environment.nodes.find { it.getConcentration(SimpleMolecule("Target")) == targetId }
            ?: error("Target $targetId not found")
        val position: Position<Euclidean2DPosition> = environment.makePosition(to.asList())
        environment.moveNodeToPosition(targetNode, position as Euclidean2DPosition)
    }
}
