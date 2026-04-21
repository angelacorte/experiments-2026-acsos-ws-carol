package it.unibo.collektive.alchemist

import com.github.benmanes.caffeine.cache.Caffeine
import com.github.benmanes.caffeine.cache.LoadingCache
import it.unibo.alchemist.model.Environment
import it.unibo.alchemist.model.Layer
import it.unibo.alchemist.model.Position
import it.unibo.alchemist.model.molecules.SimpleMolecule
import it.unibo.collektive.alchemist.device.sensors.impl.SolverProperty
import it.unibo.collektive.solver.Solver
import it.unibo.collektive.solver.gurobi.QpSettings

/**
* Stores one [SolverProperty] instance per simulation environment so QP models can be reused across steps.
*/
object SimulationSolver {
    private val activeSolver: LoadingCache<Environment<*, *>, Solver> = Caffeine.newBuilder()
        .weakKeys()
        .build { environment ->
            val layer: Layer<*, *> = requireNotNull(environment.layers[SimpleMolecule("QPSettings")])
            val origin: Position<*> = environment.makePosition(0, 0)
            layer as Layer<*, Position<*>>
            val settings = layer.getValue(origin)
            require(settings is QpSettings)
            SolverProperty(settings, environment.nodes.first())
        }

    /**
     * Returns the solver already associated with this environment.
     *
     * @throws IllegalStateException if no solver has been created for the environment yet.
     */
    val Environment<*, *>.solver: Solver
        get() = activeSolver[this]
}
