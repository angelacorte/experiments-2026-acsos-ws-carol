@file:Suppress("MatchingDeclarationName", "TooGenericExceptionCaught")

package it.unibo.alchemist.model.monitors

import java.io.File
import java.util.Locale

/**
 * One CSV row, kept generic so monitors can export different simulation views without ad-hoc writers.
 *
 * @property values values to write as cells in the CSV row
 */
data class Line(val values: List<Any?>) {
    constructor(vararg values: Any?) : this(values.toList())
}

private fun writeCsv(path: String, header: String, rowFormatter: (Line) -> String, lines: Iterable<Line>) {
    val output = File(path)
    output.parentFile?.let { parent ->
        if (!parent.exists() && !parent.mkdirs()) error("Cannot create output directory: ${parent.path}")
    }
    output.bufferedWriter().use { writer ->
        writer.appendLine(header)
        lines.forEach { line ->
            writer.appendLine(rowFormatter(line))
        }
    }
}

/**
 * Replaces the old zebra-estimation export support with a small CSV utility used by the simulation monitors.
 */
fun exportToCsv(path: String, header: String, lines: Iterable<Line>) {
    try {
        writeCsv(path, header, { line -> line.values.joinToString(separator = ",") { it.toCsvCell() } }, lines)
    } catch (e: Exception) {
        println("Cannot export CSV at $path: ${e.message}")
    }
}

/**
 * Compatibility overload for monitors ported from older experiments.
 */
fun exportToCsv(path: String, header: String, format: String, lines: Iterable<Line>) {
    try {
        writeCsv(path, header, { line -> format.format(Locale.US, *line.values.toTypedArray()) }, lines)
    } catch (e: Exception) {
        println("Cannot export CSV at $path: ${e.message}")
    }
}

/**
 * Formats numbers consistently and escapes string fields when needed.
 */
fun Any?.toCsvCell(): String = when (this) {
    null -> ""
    is Float -> "%.6f".format(Locale.US, this)
    is Double -> "%.6f".format(Locale.US, this)
    is Number, is Boolean -> toString()
    else -> toString().let { value ->
        if (value.any { it == ',' || it == '"' || it == '\n' || it == '\r' }) {
            "\"${value.replace("\"", "\"\"")}\""
        } else {
            value
        }
    }
}
