package it.unibo.collektive.model

/**
 * Static target used as navigation goal, identified thanks to its [id].
 * [position] represent its coordinates [x] [y].
 */
data class Target(
    override val x: Double,
    override val y: Double,
    val id: Number,
    val position: Coordinate = Coordinate(x, y),
) : Vector2D
