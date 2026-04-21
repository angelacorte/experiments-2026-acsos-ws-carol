package it.unibo.collektive.solver.gurobi

import com.gurobi.gurobi.GRB
import com.gurobi.gurobi.GRBModel
import com.gurobi.gurobi.GRBQuadExpr
import java.io.File

/**
 * Writes Gurobi model artifacts to the `logging` folder and enables solver logging.
 */
fun GRBModel.setupLogger() {
    val folder = File("logging")
    if (!folder.exists()) {
        val created = folder.mkdirs()
        if (!created) {
            println("Warning: could not create logging directory: ${folder.absolutePath}")
        }
    }
    write(File(folder, "debug_model.lp").path)
    write(File(folder, "debug_model.mps").path)
    env.set(GRB.IntParam.OutputFlag, 1)
    env.set(GRB.StringParam.LogFile, File(folder, "gurobi.log").path)
}

/**
 * Gold-standard logger for CLF–CBF–QP debugging (Java/Kotlin API compliant).
 *
 * Prints:
 *  - model status and size
 *  - variables (X, RC, bounds)
 *  - linear constraints (expr, slack, dual)
 *  - quadratic constraints (linear part + dual)
 *  - objective (quadratic form, if accessible)
 *
 * NOTE:
 * Quadratic terms of QConstr are NOT accessible via Gurobi Java API.
 * Use model.write("debug.lp") to inspect them.
 */
fun GRBModel.debugLoggerCLFCBF() {
    update()
    println("\n================= QP DEBUG LOGGER =================")
    val status = get(GRB.IntAttr.Status)
    println("Status       : $status")
    println("NumVars      : ${get(GRB.IntAttr.NumVars)}")
    println("NumConstrs   : ${get(GRB.IntAttr.NumConstrs)}")
    println("NumQConstrs : ${get(GRB.IntAttr.NumQConstrs)}")
    if (status == GRB.OPTIMAL) {
        println("ObjVal       : ${get(GRB.DoubleAttr.ObjVal)}")
    }
    println("---- VARIABLES (X | RC | bounds) ----")
    vars.forEach { v ->
        println(
            "${v.get(GRB.StringAttr.VarName)} : " +
                "X=${v.get(GRB.DoubleAttr.X)}, " +
                "[${v.get(GRB.DoubleAttr.LB)}, ${v.get(GRB.DoubleAttr.UB)}]",
        )
    }
    println("---- LINEAR CONSTRAINTS (expr | slack | dual) ----")
    constrs.forEach { c ->
        val row = getRow(c)
        val sense = c.get(GRB.CharAttr.Sense)
        val rhs = c.get(GRB.DoubleAttr.RHS)
        val slack = c.get(GRB.DoubleAttr.Slack)
        val expr = StringBuilder()
        for (i in 0 until row.size()) {
            expr.append("${row.getCoeff(i)} * ${row.getVar(i).get(GRB.StringAttr.VarName)}")
            if (i < row.size() - 1) expr.append(" + ")
        }
        println(
            "${c.get(GRB.StringAttr.ConstrName)} : " +
                "$expr $sense $rhs | slack=$slack | ",
        )
    }
    println("---- QUADRATIC CONSTRAINTS (linear part | dual) ----")
    qConstrs.forEach { qc ->
        val lin = getQCRow(qc)
        val rhs = qc.get(GRB.DoubleAttr.QCRHS)
        val sense = qc.get(GRB.CharAttr.QCSense)
        println("QConstr ${qc.get(GRB.StringAttr.QCName)} ")
        if (lin.size() > 0) {
            println("  Linear part:")
            for (i in 0 until lin.size()) {
                println(
                    "    ${lin.getCoeff(i)} * ${lin.getVar1(i).get(GRB.StringAttr.VarName)}" +
                        "    ${lin.getCoeff(i)} * ${lin.getVar2(i).get(GRB.StringAttr.VarName)}" +
                        "    ${lin.getCoeff(i)} * ${lin.value}",
                )
            }
        } else {
            println("  Linear part: <none>")
        }
        println("  $sense $rhs")
        println("  (quadratic terms not accessible via Java API)")
    }
    println("---- OBJECTIVE FUNCTION ----")
    val obj = objective
    when (obj) {
        is GRBQuadExpr -> {
            for (i in 0 until obj.size()) {
                println(
                    "${obj.getCoeff(i)} * " +
                        "${obj.getVar1(i).get(GRB.StringAttr.VarName)} * " +
                        "${obj.getVar2(i).get(GRB.StringAttr.VarName)}",
                )
            }
        }

        else -> println(obj.toString())
    }
    println("================= END DEBUG LOGGER =================\n")
}

/**
 * Computes the Irreducible Inconsistent Subsystem (IIS) for an infeasible model
 * and writes it to a file with the specified [fileName] inside the `logging` directory.
 *
 * @param fileName the name of the file (e.g., "localModel.ilp") where the IIS will be saved.
 */
fun GRBModel.writeIIS(fileName: String) {
    val folder = File("logging")
    folder.mkdirs()
    computeIIS()
    write(File(folder, fileName).path)
}
