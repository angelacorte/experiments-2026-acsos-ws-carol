package it.unibo.collektive.alchemist.device.sensors.impl

import com.gurobi.gurobi.GRB
import com.gurobi.gurobi.GRBEnv
import com.gurobi.gurobi.GRBModel
import it.unibo.alchemist.model.Node
import it.unibo.alchemist.model.NodeProperty
import it.unibo.collektive.admm.DualParams
import it.unibo.collektive.admm.LocalDualUpdate
import it.unibo.collektive.admm.SuggestedControl
import it.unibo.collektive.control.cbf.CBF
import it.unibo.collektive.control.clf.CLF
import it.unibo.collektive.model.Device
import it.unibo.collektive.model.SpeedControl2D
import it.unibo.collektive.solver.Solver
import it.unibo.collektive.solver.gurobi.LocalQP
import it.unibo.collektive.solver.gurobi.PairwiseQP
import it.unibo.collektive.solver.gurobi.QpSettings
import it.unibo.collektive.solver.gurobi.setLicense
import it.unibo.collektive.solver.gurobi.setupLogger

/**
 * High-level facade that owns the reusable Gurobi environments and QP templates used by ADMM.
 *
 * A solver lazily builds one local model and one pairwise model, then updates and solves them at each step.
 *
 * @property settings numerical and logging configuration shared by every managed QP.
 */
class SolverProperty<T>(override val settings: QpSettings, override val node: Node<T>) :
    Solver,
    NodeProperty<T> {

    private lateinit var local: LocalQP

    private lateinit var pairwise: PairwiseQP

    private val env: GRBEnv = setLicense().let {
        GRBEnv(true).also { env ->
            env.set(GRB.IntParam.OutputFlag, if (settings.logEnabled) 1 else 0)
            env.start()
        }
    }

    override val isLocalModelAvailable: Boolean get() = this::local.isInitialized

    override val isPairwiseModelAvailable: Boolean get() = this::pairwise.isInitialized

    override fun setupLocalModel(device: Device, localCLFs: List<CLF>, localCBFs: List<CBF>) {
        if (!isLocalModelAvailable) {
            val model = GRBModel(env).also { if (settings.logEnabled) it.setupLogger() }
            local = LocalQP.create(model, device, localCLFs, localCBFs)
        } else {
            local.syncControlFunctions(localCLFs, localCBFs)
        }
    }

    override fun setupPairwiseModel(device: Device, otherDevice: Device, pairwiseCBFs: List<CBF>) {
        if (!isPairwiseModelAvailable) {
            val model = GRBModel(env).also { if (settings.logEnabled) it.setupLogger() }
            pairwise = PairwiseQP.create(model, device, otherDevice, pairwiseCBFs)
        }
    }

    override fun <ID : Comparable<ID>> updateAndSolveLocal(
        device: Device,
        uNominal: DoubleArray,
        duals: Map<ID, DualParams>,
        deltaTime: Double,
    ): SpeedControl2D = local.updateAndSolve(device, uNominal, duals, settings, deltaTime)

    override fun updateAndSolvePairwise(
        device: Device,
        otherDevice: Device,
        duals: LocalDualUpdate,
        deltaTime: Double,
    ): SuggestedControl = pairwise.updateAndSolve(device, otherDevice, duals, settings, deltaTime)

    override fun cloneOnNewNode(node: Node<T>): NodeProperty<T> = SolverProperty(settings, node)
}
