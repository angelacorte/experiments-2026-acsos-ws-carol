package it.unibo.collektive.alchemist.device.sensors

import it.unibo.collektive.model.Coordinate
import it.unibo.collektive.model.Target

/**
 * A sensor that provides location-related information within the environment.
 */
interface LocationSensor {
    /**
     * Returns the coordinates of the node's position inside the environment.
     */
    fun coordinates(): Coordinate

    /**
     * Returns the coordinates of the neighborhood.
     */
    fun surroundings(): List<Coordinate>

    /**
     * Returns position(s) of the targets in the environment.
     */
    fun targetsPosition(): List<Target>
}
