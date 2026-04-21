package it.unibo.collektive.alchemist.device.sensors

import kotlin.time.ExperimentalTime
import kotlin.time.Instant

/**
 * Abstraction over the simulation time.
 *
 * In Alchemist-backed experiments, the time is sourced from the current simulation clock.
 * Exposing it through an interface makes it easy to inject a node property as a sensor.
 */
interface TimeSensor {
    /**
     * @return the current simulation time expressed as seconds (as a [Double]).
     */
    fun getTimeAsDouble(): Double

    /**
     * Same concept as [getTimeAsDouble], but expressed as a Kotlin [Instant].
     *
     * This is handy when using APIs that require time instants (e.g., time replication).
     */
    @OptIn(ExperimentalTime::class)
    fun getTimeAsInstant(): Instant
}
