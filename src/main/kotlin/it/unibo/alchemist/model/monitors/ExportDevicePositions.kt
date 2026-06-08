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
import java.util.Locale

/**
 * Exports the scene state over time so experiments can be plotted outside the Alchemist GUI.
 *
 * Each step appends one row per robot with its latest position, so the resulting CSVs can be
 * plotted as trajectories without rewriting the whole file at every monitor callback.
 *
 * @property dataPath destination directory for generated CSV files
 */
@Suppress("unused")
class ExportDevicePositions<T>(val seed: Double = 0.0, val dataPath: String) :
    OutputMonitor<T, Euclidean2DPosition> {

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
                        writer.appendLine("step,time,nodeId,X,Y,safeMargin,commDistance")
                    }
                }
        } catch (e: Exception) {
            println("Error resetting device CSVs: ${e.message}")
        }
    }

    private fun ensureOutputDirectory() {
        val outputDir = File(dataPath)
        if (!outputDir.exists() && !outputDir.mkdirs()) error("Cannot create output directory: $dataPath")
    }

    private fun appendPosition(nodeId: Int, time: Time, step: Long, position: Coordinate, safeMargin: Double, commDistance: Double) {
        val outputFile = File(dataPath, "positions_node-$nodeId.csv")
        val writeHeader = !outputFile.exists() || outputFile.length() == 0L
        FileWriter(outputFile, true).buffered().use { writer ->
            if (writeHeader) {
                writer.appendLine("step,time,nodeId,X,Y,safeMargin,commDistance")
            }
            writer.appendLine(
                "${step},${String.format(Locale.US, "%.6f", time.toDouble())},$nodeId,${String.format(Locale.US, "%.4f", position.x)},${String.format(Locale.US, "%.4f", position.y)},${String.format(Locale.US, "%.4f", safeMargin)},${String.format(Locale.US, "%.4f", commDistance)}"
            )
        }
    }

    override fun stepDone(
        environment: Environment<T?, Euclidean2DPosition>,
        reaction: Actionable<T?>?,
        time: Time,
        step: Long
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
                appendPosition(mid, time, step, Coordinate(position.x, position.y), safeMargin, commDistance)
            }
        } catch (e: Exception) {
            println(e.message)
        }
    }

    override fun finished(environment: Environment<T?, Euclidean2DPosition>, time: Time, step: Long) {
        ensureOutputDirectory()
        println("Export positions appended at $dataPath")
    }
}
