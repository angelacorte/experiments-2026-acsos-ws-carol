import java.util.Locale
import org.gradle.kotlin.dsl.withType
import org.jetbrains.kotlin.gradle.tasks.KotlinCompilationTask

plugins {
    application
    alias(libs.plugins.gitSemVer)
    alias(libs.plugins.collektive)
    alias(libs.plugins.kotlin.jvm)
    alias(libs.plugins.kotlin.qa)
    alias(libs.plugins.multiJvmTesting)
    alias(libs.plugins.taskTree)
}

repositories {
    mavenCentral()
}

sourceSets {
    main {
        dependencies {
            implementation(libs.bundles.alchemist)
            implementation(libs.caffeine)
            implementation(libs.bundles.collektive)
            implementation(libs.gurobi)
        }
        resources {
            srcDir("src/main/yaml")
        }
    }
}

multiJvm {
    jvmVersionForCompilation.set(17)
}

// Heap size estimation for batches
val maxHeap: Long? by project
val heap: Long =
    maxHeap
        ?: if (System.getProperty("os.name").lowercase().contains("linux")) {
            File("/proc/meminfo")
                .useLines { lines ->
                    lines.firstOrNull { it.startsWith("MemAvailable:") }
                        ?.trim()
                        ?.split(Regex("\\s+"))
                        ?.getOrNull(1)
                        ?.toLong()
                        ?.let { it / 1024 }
                        ?: error("MemAvailable not found in /proc/meminfo")
                }
                .toString()
                .trim()
                .toLong()
                .also { println("Detected ${it}MB RAM available.") } * 9 / 10
        } else {
            // Guess 16GB RAM of which 2 used by the OS
            14 * 1024L
        }
val taskSizeFromProject: Int? by project
val taskSize = taskSizeFromProject ?: 512
val threadCount = maxOf(1, minOf(Runtime.getRuntime().availableProcessors(), heap.toInt() / taskSize))
val alchemistGroupBatch = "Run batch simulations"
val alchemistGroupGraphic = "Run graphic simulations with Alchemist"

/*
 * This task is used to run all experiments in sequence
 */
val runAllGraphic by tasks.register<DefaultTask>("runAllGraphic") {
    group = alchemistGroupGraphic
    description = "Launches all simulations with the graphic subsystem enabled"
}
val runAllBatch by tasks.register<DefaultTask>("runAllBatch") {
    group = alchemistGroupBatch
    description = "Launches all experiments"
}

fun String.capitalizeString(): String = this.replaceFirstChar {
    if (it.isLowerCase()) {
        it.titlecase(Locale.getDefault())
    } else {
        it.toString()
    }
}

/*
 * Scan the folder with the simulation files, and create a task for each one of them.
 */
File(rootProject.rootDir.path + "/src/main/yaml")
    .listFiles()
    ?.filter { it.extension == "yml" }
    ?.sortedBy { it.nameWithoutExtension }
    ?.forEach {
        fun basetask(name: String, additionalConfiguration: JavaExec.() -> Unit = {}) = tasks.register<JavaExec>(name) {
            description = "Launches graphic simulation ${it.nameWithoutExtension}"
            mainClass.set("it.unibo.alchemist.Alchemist")
            classpath = sourceSets["main"].runtimeClasspath
            args("run", it.absolutePath)
            if (System.getenv("CI") == "true") {
                args("--override", "terminate: { type: AfterTime, parameters: [2] } ")
            } else {
                this.additionalConfiguration()
            }
        }
        val capitalizedName = it.nameWithoutExtension.capitalizeString()
        val graphic by basetask("run${capitalizedName}Graphic") {
            group = alchemistGroupGraphic
            args(
                "--override",
                "monitors: { type: SwingGUI, parameters: { graphics: effects/${it.nameWithoutExtension}.json } }",
                "--override",
                "launcher: { parameters: { batch: [], autoStart: false } }",
                "--verbosity",
                "error",
            )
        }
        runAllGraphic.dependsOn(graphic)
        val batch by basetask("run${capitalizedName}Batch") {
            group = alchemistGroupBatch
            description = "Launches batch experiments for $capitalizedName"
            maxHeapSize = "${minOf(heap.toInt(), Runtime.getRuntime().availableProcessors() * taskSize)}m"
            File("data").mkdirs()
            args(
                "--verbosity",
                "error",
            )
        }
        runAllBatch.dependsOn(batch)
    }

tasks.withType<KotlinCompilationTask<*>>().all {
    compilerOptions {
        allWarningsAsErrors = false
        freeCompilerArgs.add("-Xcontext-parameters")
    }
}
