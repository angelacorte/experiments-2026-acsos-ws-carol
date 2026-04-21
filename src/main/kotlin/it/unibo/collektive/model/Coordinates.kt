package it.unibo.collektive.model

/**
 * 2D [dimension] point-like contract exposing coordinates and
 * a self-referencing [position] for DSLs that expect a `([x], [y])` pair.
 */
interface Vector2D {
    val x: Double
    val y: Double

    val dimension: Int
        get() = 2
}

/**
 * Basic agnostic [x], [y] coordinates.
 */
data class Coordinate(override val x: Double, override val y: Double) : Vector2D {
    override fun toString(): String = "Coord($x, $y)"
}

/**
 * Planar control input.
 */
data class SpeedControl2D(override val x: Double, override val y: Double) : Vector2D {
    override fun toString(): String = "Control($x, $y)"
}

/**
 * Zero-initialized position.
 */
fun initVector2D(): Coordinate = Coordinate(0.0, 0.0)

/**
 * Zero control input utility.
 */
fun zeroSpeed(): SpeedControl2D = SpeedControl2D(0.0, 0.0)
