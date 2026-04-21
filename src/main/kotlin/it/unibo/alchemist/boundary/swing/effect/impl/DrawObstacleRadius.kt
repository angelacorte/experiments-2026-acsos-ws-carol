@file:Suppress("DEPRECATION", "MagicNumber")

package it.unibo.alchemist.boundary.swing.effect.impl

import it.unibo.alchemist.boundary.swingui.effect.api.Effect
import it.unibo.alchemist.boundary.ui.api.Wormhole2D
import it.unibo.alchemist.model.Environment
import it.unibo.alchemist.model.Node
import it.unibo.alchemist.model.Position2D
import it.unibo.alchemist.model.Time
import it.unibo.alchemist.model.molecules.SimpleMolecule
import java.awt.Color
import java.awt.Graphics2D
import java.awt.Point
import kotlin.math.abs
import kotlin.math.max
import kotlin.math.nextUp

/**
 * Swing effect that renders robot safe margins and obstacle safety radii on the 2D view.
 *
 * It reads concentrations for `Robot`, `Obstacle`, `SafeMargin`, and `SafeRadius` molecules and
 * draws concentric circles to visualize footprint and avoidance regions.
 */
class DrawObstacleRadius : Effect {
    override fun getColorSummary(): Color = Color.BLACK

    /**
     * Last time that the effect has been updated.
     */
    @Transient
    var lastUpdated = Time.NEGATIVE_INFINITY

    override fun <T : Any?, P : Position2D<P>> apply(
        graphics: Graphics2D,
        node: Node<T>,
        environment: Environment<T, P>,
        wormhole: Wormhole2D<P>,
    ) {
        if (environment.simulation.time != lastUpdated) {
            lastUpdated = environment.simulation.time
        }
        runCatching { renderNode(graphics, node, environment, wormhole) }
    }

    private fun <T : Any?, P : Position2D<P>> renderNode(
        graphics: Graphics2D,
        node: Node<T>,
        environment: Environment<T, P>,
        wormhole: Wormhole2D<P>,
    ) {
        val nodePosition = environment.getPosition(node)
        val viewPoint = wormhole.getViewPoint(nodePosition)
        val isRobot = node.contains(robot)
        val isObstacle = node.contains(obstacle)
        val margin = node.getConcentration(safeMargin).toDouble()
        val radius = readRadius(node)
        val communicationDistance = readCommunicationDistance(node)
        val baseDrawSize = drawSize(isRobot, isObstacle, margin, radius)
        val visibilityDrawSize =
            if (isRobot && communicationDistance > 0.0) max(baseDrawSize, communicationDistance) else baseDrawSize
        val visibilitySizeInScreen = toScreenSize(visibilityDrawSize, nodePosition, viewPoint, environment, wormhole)
        if (!isVisible(viewPoint, visibilitySizeInScreen, wormhole)) return
        val baseSizeInScreen = toScreenSize(baseDrawSize, nodePosition, viewPoint, environment, wormhole)
        if (isRobot && communicationDistance > 0.0) {
            drawCommunicationArea(
                graphics,
                environment,
                wormhole,
                viewPoint,
                nodePosition,
                communicationDistance,
            )
        }
        if (isRobot) drawRobot(graphics, viewPoint, baseSizeInScreen)
        if (isObstacle) {
            drawObstacle(
                graphics,
                environment,
                wormhole,
                viewPoint,
                radius,
                nodePosition,
                baseSizeInScreen,
            )
        }
    }

    private fun drawRobot(graphics: Graphics2D, viewPoint: Point, sizeInScreenCoordinates: Point) {
        graphics.color = Color.GRAY // hsbColor(60f, alpha = 0.3f)
        graphics.drawOval(
            viewPoint.x - sizeInScreenCoordinates.x / 2,
            viewPoint.y - sizeInScreenCoordinates.y / 2,
            sizeInScreenCoordinates.x,
            sizeInScreenCoordinates.y,
        )
    }

    private fun <P : Position2D<P>> drawCommunicationArea(
        graphics: Graphics2D,
        environment: Environment<*, P>,
        wormhole: Wormhole2D<P>,
        viewPoint: Point,
        nodePosition: P,
        communicationDistance: Double,
    ) {
        val commSizeAsPosition: P = environment.makePosition(communicationDistance, communicationDistance)
        val commSizeFromLocation = commSizeAsPosition + nodePosition.coordinates
        val commSizeInScreen =
            (wormhole.getViewPoint(commSizeFromLocation) - viewPoint)
                .let { Point(abs(it.x), abs(it.y)) }
                .takeIf { it.x > MIN_NODE_SIZE && it.y > MIN_NODE_SIZE }
                ?: Point(MIN_NODE_SIZE, MIN_NODE_SIZE)
        graphics.color = hsbColor(hueDeg = 0f, saturation = 0f, brightness = 0.85f, alpha = 0.2f)
        graphics.fillOval(
            viewPoint.x - commSizeInScreen.x,
            viewPoint.y - commSizeInScreen.y,
            2 * commSizeInScreen.x,
            2 * commSizeInScreen.y,
        )
    }

    private fun <P : Position2D<P>> drawObstacle(
        graphics: Graphics2D,
        environment: Environment<*, P>,
        wormhole: Wormhole2D<P>,
        viewPoint: Point,
        radius: Double,
        nodePosition: P,
        sizeInScreenCoordinates: Point,
    ) {
//        graphics.color = Color.ORANGE // hsbColor(30f, alpha = 0.4f)
        graphics.color = hsbColor(55f, alpha = 0.2f)
        graphics.fillOval(
            viewPoint.x - sizeInScreenCoordinates.x,
            viewPoint.y - sizeInScreenCoordinates.y,
            2 * sizeInScreenCoordinates.x,
            2 * sizeInScreenCoordinates.y,
        )
        val innerSizeAsPosition: P = environment.makePosition(radius, radius)
        val innerSizeFromLocation = innerSizeAsPosition + nodePosition.coordinates
        val innerSizeScreen =
            (wormhole.getViewPoint(innerSizeFromLocation) - viewPoint)
                .let { Point(abs(it.x), abs(it.y)) }
                .takeIf { it.x > MIN_NODE_SIZE && it.y > MIN_NODE_SIZE }
                ?: Point(MIN_NODE_SIZE, MIN_NODE_SIZE)

        graphics.color = hsbColor(0f, alpha = 0.7f)
//        graphics.color = Color.RED//hsbColor(0f, alpha = 0.5f)
        graphics.fillOval(
            viewPoint.x - innerSizeScreen.x,
            viewPoint.y - innerSizeScreen.y,
            2 * innerSizeScreen.x,
            2 * innerSizeScreen.y,
        )
    }

    private fun drawSize(isRobot: Boolean, isObstacle: Boolean, margin: Double, radius: Double): Double = when {
        isRobot && isObstacle -> radius + margin
        isRobot -> margin
        isObstacle -> radius + margin
        else -> 0.0.nextUp()
    }

    private fun <P : Position2D<P>> toScreenSize(
        drawSize: Double,
        nodePosition: P,
        viewPoint: Point,
        environment: Environment<*, P>,
        wormhole: Wormhole2D<P>,
    ): Point {
        val sizeAsPosition: P = environment.makePosition(drawSize, drawSize)
        val sizeFromLocation = sizeAsPosition + nodePosition.coordinates
        return (wormhole.getViewPoint(sizeFromLocation) - viewPoint)
            .let { Point(abs(it.x), abs(it.y)) }
            .takeIf { it.x > MIN_NODE_SIZE && it.y > MIN_NODE_SIZE }
            ?: Point(MIN_NODE_SIZE, MIN_NODE_SIZE)
    }

    private fun isVisible(viewPoint: Point, sizeInScreenCoordinates: Point, wormhole: Wormhole2D<*>): Boolean {
        val boundingBoxSize = sizeInScreenCoordinates / 2
        val boundingBox =
            listOf(
                viewPoint + boundingBoxSize,
                viewPoint + boundingBoxSize.mirrorX(),
                viewPoint + boundingBoxSize.mirrorY(),
                viewPoint - boundingBoxSize,
            )
        return boundingBox.any { wormhole.isInsideView(it) }
    }

    private fun readRadius(node: Node<*>): Double =
        (if (node.contains(safeRadius)) node.getConcentration(safeRadius) else 0.0) as Double

    private fun readCommunicationDistance(node: Node<*>): Double =
        (if (node.contains(communicationDistance)) node.getConcentration(communicationDistance) else 0.0).toDouble()

    /**
     * Shared molecules and rendering constants for the effect.
     */
    companion object {
        /**
         * Helper molecule flag identifying robot nodes.
         */
        val robot = SimpleMolecule("Robot")

        /** Safe margin molecule key used to size the footprint. */
        val safeMargin = SimpleMolecule("SafeMargin")

        /** Obstacle molecule key. */
        val obstacle = SimpleMolecule("Obstacle")

        /** Safety radius molecule key. */
        val safeRadius = SimpleMolecule("SafeRadius")

        /**
         *
         */
        val communicationDistance = SimpleMolecule("CommunicationDistance")

        /** Minimum diameter (in pixels) used when drawing circles. */
        const val MIN_NODE_SIZE = 1

        private fun Any?.toInt(): Int? = when (this) {
            is Int -> this
            is Number -> this.toInt()
            is String -> this.toInt()
            null -> null
            Unit -> null
            else -> error("Unexpected integer: $this")
        }

        private fun Any?.toDouble(): Double = when (this) {
            is Double -> this
            is Number -> this.toDouble()
            null -> 0.0
            Unit -> 0.0
            else -> error("Unexpected integer: $this")
        }

        private operator fun Point.plus(other: Point): Point = Point(x + other.x, y + other.y)

        private operator fun Point.minus(other: Point): Point = Point(x - other.x, y - other.y)

        private operator fun Point.div(factor: Int): Point = Point((x / factor), (y / factor))

        private fun Point.mirrorX(): Point = Point(-x, y)

        private fun Point.mirrorY(): Point = Point(x, -y)

        /**
         * Utility to create an HSB color with an alpha channel.
         */
        fun hsbColor(hueDeg: Float, alpha: Float, saturation: Float = 1f, brightness: Float = 1f): Color {
            val rgb = Color.HSBtoRGB(hueDeg / 360f, saturation, brightness)
            val red = (rgb shr RED_SHIFT) and COLOR_MASK
            val green = (rgb shr GREEN_SHIFT) and COLOR_MASK
            val blue = rgb and COLOR_MASK
            val alphaChannel = (alpha * MAX_ALPHA).toInt()
            return Color(red, green, blue, alphaChannel)
        }

        private const val COLOR_MASK = 0xFF
        private const val RED_SHIFT = 16
        private const val GREEN_SHIFT = 8
        private const val MAX_ALPHA = 255
    }
}
