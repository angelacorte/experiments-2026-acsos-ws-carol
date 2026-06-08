package it.unibo.alchemist.model.monitors

import it.unibo.alchemist.boundary.OutputMonitor
import it.unibo.alchemist.model.Environment
import it.unibo.alchemist.model.Time
import it.unibo.alchemist.model.molecules.SimpleMolecule
import it.unibo.alchemist.model.positions.Euclidean2DPosition
import java.io.File
import java.io.FileWriter
import java.util.Locale

@Suppress("unused")
class ExportObjectsPosition<T>(val dataPath: String) :
    OutputMonitor<T, Euclidean2DPosition>  {

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

    private fun appendTarget(targetId: Int, time: Time, step: Long, position: Euclidean2DPosition) {
        val file = File(dataPath, "target-$targetId.csv")
        val row = listOf(
            step,
            String.format(Locale.US, "%.6f", time.toDouble()),
            targetId,
            String.format(Locale.US, "%.4f", position.x),
            String.format(Locale.US, "%.4f", position.y),
        ).joinToString(",")
        appendCsvRow(file, "step,time,id,x,y", row)
    }

    private fun appendObstacle(obstacleId: Int, time: Time, step: Long, position: Euclidean2DPosition, radius: Double, margin: Double) {
        val file = File(dataPath, "obstacle-$obstacleId.csv")
        val row = listOf(
            step,
            String.format(Locale.US, "%.6f", time.toDouble()),
            obstacleId,
            String.format(Locale.US, "%.4f", position.x),
            String.format(Locale.US, "%.4f", position.y),
            String.format(Locale.US, "%.4f", radius),
            String.format(Locale.US, "%.4f", margin),
        ).joinToString(",")
        appendCsvRow(file, "step,time,id,x,y,radius,margin", row)
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
                    appendObstacle(
                        obstacle.id,
                        time,
                        step,
                        position,
                        obstacle.getConcentration(SimpleMolecule("SafeRadius")).asDouble(),
                        obstacle.getConcentration(SimpleMolecule("SafeMargin")).asDouble(),
                    )
                }

            environment.nodes
                .filter { it.contains(SimpleMolecule("Target")) }
                .forEach { target ->
                    val targetID = target.getConcentration(SimpleMolecule("Target")) as Int
                    appendTarget(targetID, time, step, environment.getPosition(target))
                }
        } catch (e: Exception) {
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
                        writer.appendLine("step,time,id,x,y,radius,margin")
                    }
                }
            environment.nodes
                .filter { it.contains(SimpleMolecule("Target")) }
                .forEach { tg ->
                    val id = try {
                        (tg.getConcentration(SimpleMolecule("Target")) as? Number)?.toInt() ?: tg.id
                    } catch (_: Exception) { tg.id }
                    val file = File(dataPath, "target-$id.csv")
                    FileWriter(file, false).buffered().use { writer ->
                        writer.appendLine("step,time,id,x,y")
                    }
                }
        } catch (e: Exception) {
            println("Error resetting object CSVs: ${e.message}")
        }
    }
}

