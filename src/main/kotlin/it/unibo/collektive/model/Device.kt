package it.unibo.collektive.model

/**
 * Mobile agent with a control vector and safety envelope.
 * A robot has a [safeMargin], a [control] that represent the current vector of speed, and the [maxSpeed] applicable.
 * [position] represent its coordinates [x] [y].
 */
data class Device(
    override val x: Double,
    override val y: Double,
    val safeMargin: Double,
    val control: SpeedControl2D = SpeedControl2D(0.0, 0.0),
    val maxSpeed: Double = Double.MAX_VALUE,
) : Vector2D {
    val position: Coordinate get() = Coordinate(x, y)
}
