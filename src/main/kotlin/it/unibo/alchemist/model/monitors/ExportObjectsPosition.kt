package it.unibo.alchemist.model.monitors

import it.unibo.alchemist.boundary.OutputMonitor
import it.unibo.alchemist.model.Environment
import it.unibo.alchemist.model.Time
import it.unibo.alchemist.model.molecules.SimpleMolecule
import it.unibo.alchemist.model.positions.Euclidean2DPosition
import java.io.File
import java.io.FileWriter
import java.io.IOException
import java.util.Locale
import kotlin.math.roundToLong

/**
 * Exports obstacle and target positions to CSV files during a simulation.
 *
 * A separate CSV file is maintained for each obstacle and target so their positions can be
 * reconstructed independently across simulation ticks.
 *
 * @property dataPath destination directory for generated CSV files
 */
@Suppress("unused")
class ExportObjectsPosition<T>(val dataPath: String) : OutputMonitor<T, Euclidean2DPosition> {

    private val lastExportedObstacleTick: MutableMap<Int, Long> = mutableMapOf()
    private val lastExportedTargetTick: MutableMap<Int, Long> = mutableMapOf()

    private fun ensureOutputDirectory() {
        val outputDir = File(dataPath)
        if (!outputDir.exists() && !outputDir.mkdirs()) error("Cannot create output directory: $dataPath")
    }

    private fun appendCsvRow(file: File, header: String, row: String) {
        val writeHeader = !file.exists() || file.length() == 0L
        FileWriter(file, true).buffered().use { writer ->
            if (writeHeader) {
                writer.appendLine(header)
            }
            writer.appendLine(row)
        }
    }

    private fun Any?.asDouble(): Double = when (this) {
        is Number -> toDouble()
        else -> error("Expected numeric value, found $this")
    }

    private fun appendTarget(targetId: Int, time: Time, position: Euclidean2DPosition) {
        val file = File(dataPath, "target-$targetId.csv")
        val row = listOf(
            String.format(Locale.US, "%d", time.toDouble().roundToLong()),
            targetId,
            String.format(Locale.US, "%.4f", position.x),
            String.format(Locale.US, "%.4f", position.y),
        ).joinToString(",")
        appendCsvRow(file, "time,id,x,y", row)
    }

    private fun appendObstacle(
        obstacleId: Int,
        time: Time,
        position: Euclidean2DPosition,
        radius: Double,
        margin: Double,
    ) {
        val file = File(dataPath, "obstacle-$obstacleId.csv")
        val row = listOf(
            String.format(Locale.US, "%d", time.toDouble().roundToLong()),
            obstacleId,
            String.format(Locale.US, "%.4f", position.x),
            String.format(Locale.US, "%.4f", position.y),
            String.format(Locale.US, "%.4f", radius),
            String.format(Locale.US, "%.4f", margin),
        ).joinToString(",")
        appendCsvRow(file, "time,id,x,y,radius,margin", row)
    }

    override fun stepDone(
        environment: Environment<T?, Euclidean2DPosition>,
        reaction: it.unibo.alchemist.model.Actionable<T?>?,
        time: Time,
        step: Long,
    ) {
        try {
            ensureOutputDirectory()

            environment.nodes
                .filter { it.contains(SimpleMolecule("Obstacle")) }
                .forEach { obstacle ->
                    val position = environment.getPosition(obstacle)
                    val tick = time.toDouble().roundToLong()
                    val oid = obstacle.id
                    if (lastExportedObstacleTick[oid] != tick) {
                        appendObstacle(
                            oid,
                            time,
                            position,
                            obstacle.getConcentration(SimpleMolecule("SafeRadius")).asDouble(),
                            obstacle.getConcentration(SimpleMolecule("SafeMargin")).asDouble(),
                        )
                        lastExportedObstacleTick[oid] = tick
                    }
                }

            environment.nodes
                .filter { it.contains(SimpleMolecule("Target")) }
                .forEach { target ->
                    val tick = time.toDouble().roundToLong()
                    val targetID = try {
                        (target.getConcentration(SimpleMolecule("Target")) as? Number)?.toInt() ?: target.id
                    } catch (_: Exception) {
                        target.id
                    }
                    if (lastExportedTargetTick[targetID] != tick) {
                        appendTarget(targetID, time, environment.getPosition(target))
                        lastExportedTargetTick[targetID] = tick
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
        println("Export objects appended at $dataPath")
    }

    override fun initialized(environment: Environment<T?, Euclidean2DPosition>) {
        // Reset object CSV files at the beginning of the simulation so previous runs
        // do not accumulate in the same files.
        try {
            ensureOutputDirectory()
            environment.nodes
                .filter { it.contains(SimpleMolecule("Obstacle")) }
                .forEach { obs ->
                    val file = File(dataPath, "obstacle-${obs.id}.csv")
                    FileWriter(file, false).buffered().use { writer ->
                        writer.appendLine("time,id,x,y,radius,margin")
                    }
                }
            environment.nodes
                .filter { it.contains(SimpleMolecule("Target")) }
                .forEach { tg ->
                    val id = try {
                        (tg.getConcentration(SimpleMolecule("Target")) as? Number)?.toInt() ?: tg.id
                    } catch (_: Exception) {
                        tg.id
                    }
                    val file = File(dataPath, "target-$id.csv")
                    FileWriter(file, false).buffered().use { writer ->
                        writer.appendLine("time,id,x,y")
                    }
                }
            lastExportedObstacleTick.clear()
            lastExportedTargetTick.clear()
        } catch (e: IOException) {
            println("Error resetting object CSVs: ${e.message}")
        } catch (e: IllegalStateException) {
            println("Error resetting object CSVs: ${e.message}")
        }
    }
}
