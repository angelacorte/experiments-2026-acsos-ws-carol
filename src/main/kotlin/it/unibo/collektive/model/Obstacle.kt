package it.unibo.collektive.model

/**
 * The [x], [y] coordinates position of an obstacle, and relative [radius] and additional [margin] of danger.
 */
data class Obstacle(override val x: Double, override val y: Double, val radius: Double, val margin: Double) : Vector2D
