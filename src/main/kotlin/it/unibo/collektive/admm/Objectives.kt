package it.unibo.collektive.admm

import com.gurobi.gurobi.GRB
import com.gurobi.gurobi.GRBException
import com.gurobi.gurobi.GRBModel
import com.gurobi.gurobi.GRBQuadExpr
import com.gurobi.gurobi.GRBVar
import it.unibo.collektive.control.ControlFunction
import it.unibo.collektive.mathutils.minus
import it.unibo.collektive.mathutils.plus
import it.unibo.collektive.mathutils.toDoubleArray
import it.unibo.collektive.model.Device
import it.unibo.collektive.model.SpeedControl2D
import it.unibo.collektive.model.zeroSpeed
import it.unibo.collektive.solver.gurobi.GRBVector
import it.unibo.collektive.solver.gurobi.QpSettings
import it.unibo.collektive.solver.gurobi.addRhoNorm2Sq
import it.unibo.collektive.solver.gurobi.writeIIS

/**
 * Common-edge ADMM QP: computes pairwise suggested controls for a neighbor pair.
 * Slack contributions are collected generically from each CF via [addSlackToObjective].
 */
fun GRBModel.minimizeADMMCommonQP(
    zi: GRBVector,
    zj: GRBVector,
    device: Device,
    other: Device,
    incidentDuals: LocalDualUpdate,
    activeSlacks: List<Pair<ControlFunction, GRBVar>> = emptyList(),
    settings: QpSettings,
): SuggestedControl {
    val obj = GRBQuadExpr()
    val ui = device.control
    val uj = other.control
    val yi = incidentDuals.yi
    val yj = incidentDuals.yj
    obj.addRhoNorm2Sq(zi, (ui + yi).toDoubleArray(), settings.rhoADMM / 2.0)
    obj.addRhoNorm2Sq(zj, (uj + yj).toDoubleArray(), settings.rhoADMM / 2.0)
    activeSlacks.forEach { (cf, slack) -> cf.addSlackToObjective(obj, slack, settings) }
    return solveCommon(obj, zi, zj, device, other)
}

/**
 * Local ADMM QP: minimizes deviation from nominal control plus slack and consensus penalties.
 *
 * @return optimal control; falls back to previous control on failure.
 */
fun <ID : Comparable<ID>> GRBModel.minimizeADMMLocalQP(
    u: GRBVector,
    uNominal: DoubleArray,
    device: Device,
    duals: Map<ID, DualParams>,
    activeSlacks: List<Pair<ControlFunction, GRBVar>>,
    settings: QpSettings,
): SpeedControl2D {
    val obj = GRBQuadExpr()
    obj.addRhoNorm2Sq(u, uNominal)
    activeSlacks.forEach { (cf, slack) -> cf.addSlackToObjective(obj, slack, settings) }
    duals.forEach { (_, value) ->
        val suggested = value.suggestedControl.zi.toDoubleArray()
        val residual = value.localDualUpdate.yi.toDoubleArray()
        obj.addRhoNorm2Sq(u, suggested - residual, settings.rhoADMM / 2.0)
    }
    return solveLocal(u, obj, device)
}

private fun GRBModel.solveLocal(u: GRBVector, obj: GRBQuadExpr, device: Device): SpeedControl2D = try {
    setObjective(obj, GRB.MINIMIZE)
    optimize()
    val status = get(GRB.IntAttr.Status)
    if (status == GRB.INFEASIBLE) {
        writeIIS("localModel.ilp")
        computeIIS()
        for (constraint in constrs) {
            if (constraint.get(GRB.IntAttr.IISConstr) == 1) {
                println("IIS constraint: ${constraint.get(GRB.StringAttr.ConstrName)}")
            }
        }
    }
    if (get(GRB.IntAttr.SolCount) > 0) {
        val uOptX = u[0].get(GRB.DoubleAttr.X)
        val uOptY = u[1].get(GRB.DoubleAttr.X)
        SpeedControl2D(uOptX, uOptY)
    } else {
        println("Local QP: no solution found (status $status)")
        device.control
    }
} catch (ex: GRBException) {
    println("${ex.message} - Minimization problem is infeasible, returning control: ${zeroSpeed()}.")
    zeroSpeed() // robot.control
}

private fun GRBModel.solveCommon(
    obj: GRBQuadExpr,
    zi: GRBVector,
    zj: GRBVector,
    device: Device,
    other: Device,
): SuggestedControl = try {
    setObjective(obj, GRB.MINIMIZE)
    optimize()
    val status = get(GRB.IntAttr.Status)
    if (status == GRB.INFEASIBLE) {
        writeIIS("commonModel.ilp")
        computeIIS()
        for (constraint in constrs) {
            if (constraint.get(GRB.IntAttr.IISConstr) == 1) {
                println("IIS constraint: ${constraint.get(GRB.StringAttr.ConstrName)}")
            }
        }
    }
    if (get(GRB.IntAttr.SolCount) > 0) {
        val zxiOpt = zi[0].get(GRB.DoubleAttr.X)
        val zyiOpt = zi[1].get(GRB.DoubleAttr.X)
        val zxjOpt = zj[0].get(GRB.DoubleAttr.X)
        val zyjOpt = zj[1].get(GRB.DoubleAttr.X)
        SuggestedControl(SpeedControl2D(zxiOpt, zyiOpt), SpeedControl2D(zxjOpt, zyjOpt))
    } else {
        println("Common QP: no solution found (status $status)")
        SuggestedControl(device.control, other.control)
    }
} catch (ex: GRBException) {
    println(
        "${ex.message} - " +
            "Minimization problem is infeasible, staying still.",
//            "Minimization problem is infeasible, return controls from local QP: ${robot.control} & ${other.control}.",
    )
    SuggestedControl(zeroSpeed(), zeroSpeed()) //    SuggestedControl(robot.control, other.control)
}
