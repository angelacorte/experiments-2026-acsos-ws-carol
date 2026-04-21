package it.unibo.collektive.solver.gurobi

import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths

/**
 * Default path for the Gurobi license file on macOS systems.
 * Used as a fallback if no environment variable or system property is set.
 */
private val DEFAULT_LICENSE_PATH: Path =
    Paths.get(System.getProperty("user.home"), "Library", "gurobi", "gurobi.lic")

/**
 * Resolves the Gurobi license file path.
 *
 * Search order:
 * 1. `GRB_LICENSE_FILE` environment variable
 * 2. `GRB_LICENSE_FILE` JVM system property
 * 3. Default location `~/Library/gurobi/gurobi.lic`
 *
 * @return the path to the Gurobi license file if found, or null otherwise
 */
private fun resolveLicensePath(): Path? = sequenceOf(
    System.getenv("GRB_LICENSE_FILE"),
    System.getProperty("GRB_LICENSE_FILE"),
).filterNotNull()
    .filter { it.isNotBlank() }
    .map { Paths.get(it) }
    .plusElement(DEFAULT_LICENSE_PATH)
    .firstOrNull { Files.exists(it) }

/**
 * Sets the `GRB_LICENSE_FILE` system property from the first discovered license file.
 *
 * This function attempts to locate the Gurobi license file using [resolveLicensePath].
 * If no license file is found, it throws an [IllegalStateException] with a descriptive error message.
 *
 * @throws IllegalStateException if no license file can be found
 */
fun setLicense() {
    val license = resolveLicensePath()
        ?: error(
            "Gurobi license not found. Set GRB_LICENSE_FILE as an environment variable " +
                "or JVM property, or place the license at '$DEFAULT_LICENSE_PATH'.",
        )
    System.setProperty("GRB_LICENSE_FILE", license.toString())
}
