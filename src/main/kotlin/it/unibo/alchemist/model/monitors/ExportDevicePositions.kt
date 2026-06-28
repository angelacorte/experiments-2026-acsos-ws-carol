package it.unibo.alchemist.model.monitors

import it.unibo.alchemist.boundary.OutputMonitor
import it.unibo.alchemist.model.Actionable
import it.unibo.alchemist.model.Environment
import it.unibo.alchemist.model.Time
import it.unibo.alchemist.model.molecules.SimpleMolecule
import it.unibo.alchemist.model.positions.Euclidean2DPosition
import it.unibo.collektive.model.Coordinate
import java.io.File
import java.io.FileWriter
import java.io.IOException
import java.util.Locale
import kotlin.math.roundToLong

/**
 * Exports the scene state over time so experiments can be plotted outside the Alchemist GUI.
 *
 * Each step appends one row per robot with its latest position, so the resulting CSVs can be
 * plotted as trajectories without rewriting the whole file at every monitor callback.
 *
 * @property dataPath destination directory for generated CSV files
 * @property seed simulation seed associated with this export, kept for monitor configuration compatibility
 */
@Suppress("unused")
class ExportDevicePositions<T>(val seed: Double = 0.0, val dataPath: String) :
    OutputMonitor<T, Euclidean2DPosition> {

    private val lastExportedTick: MutableMap<Int, Long> = mutableMapOf()

    override fun initialized(environment: Environment<T?, Euclidean2DPosition>) {
        // Reset device CSV files at the beginning of the simulation so previous runs
        // do not accumulate in the same files.
        try {
            ensureOutputDirectory()
            environment.nodes
                .filter { it.contains(SimpleMolecule("Robot")) }
                .forEach { node ->
                    val mid = node.id
                    val outputFile = File(dataPath, "positions_node-$mid.csv")
                    // Overwrite and write header
                    FileWriter(outputFile, false).buffered().use { writer ->
                        writer.appendLine("time,nodeId,X,Y,safeMargin,commDistance,isLeader")
                    }
                }
            lastExportedTick.clear()
        } catch (e: IOException) {
            println("Error resetting device CSVs: ${e.message}")
        } catch (e: IllegalStateException) {
            println("Error resetting device CSVs: ${e.message}")
        }
    }

    private fun ensureOutputDirectory() {
        val outputDir = File(dataPath)
        if (!outputDir.exists() && !outputDir.mkdirs()) error("Cannot create output directory: $dataPath")
    }

    private fun appendPosition(
        nodeId: Int,
        time: Time,
        position: Coordinate,
        safeMargin: Double,
        commDistance: Double,
        isLeader: Boolean,
    ) {
        val outputFile = File(dataPath, "positions_node-$nodeId.csv")
        val writeHeader = !outputFile.exists() || outputFile.length() == 0L
        FileWriter(outputFile, true).buffered().use { writer ->
            if (writeHeader) {
                writer.appendLine("time,nodeId,X,Y,safeMargin,commDistance,isLeader")
            }
            val tick = time.toDouble().roundToLong()
            val formattedPosition = listOf(
                String.format(Locale.US, "%.4f", position.x),
                String.format(Locale.US, "%.4f", position.y),
                String.format(Locale.US, "%.4f", safeMargin),
                String.format(Locale.US, "%.4f", commDistance),
            )
            writer.appendLine(
                listOf(
                    tick,
                    nodeId,
                    formattedPosition[0],
                    formattedPosition[1],
                    formattedPosition[2],
                    formattedPosition[3],
                    isLeader,
                )
                    .joinToString(","),
            )
        }
    }

    override fun stepDone(
        environment: Environment<T?, Euclidean2DPosition>,
        reaction: Actionable<T?>?,
        time: Time,
        step: Long,
    ) {
        try {
            ensureOutputDirectory()
            val devices = environment.nodes
                .filter { it.contains(SimpleMolecule("Robot")) }
            @Suppress("UNCHECKED_CAST")
            devices.forEach { node ->
                val mid = node.id
                val position = environment.getPosition(node)
                val safeMargin = node.getConcentration(SimpleMolecule("SafeMargin")) as? Double ?: 0.0
                val commDistance = node.getConcentration(SimpleMolecule("CommunicationDistance")) as? Double ?: 0.0
                // isLeader molecule may be absent; if present coerce value to boolean
                val isLeader: Boolean = if (node.contains(SimpleMolecule("isLeader"))) {
                    when (val c = node.getConcentration(SimpleMolecule("isLeader"))) {
                        is Boolean -> c
                        is String -> c.toBoolean()
                        is Number -> c.toInt() != 0
                        else -> false
                    }
                } else {
                    false
                }
                val tick = time.toDouble().roundToLong()
                if (lastExportedTick[mid] != tick) {
                    appendPosition(mid, time, Coordinate(position.x, position.y), safeMargin, commDistance, isLeader)
                    lastExportedTick[mid] = tick
                }
            }
        } catch (e: IOException) {
            println(e.message)
        } catch (e: IllegalStateException) {
            println(e.message)
        }
    }

    override fun finished(environment: Environment<T?, Euclidean2DPosition>, time: Time, step: Long) {
        ensureOutputDirectory()
        println("Export positions appended at $dataPath")
    }
}
