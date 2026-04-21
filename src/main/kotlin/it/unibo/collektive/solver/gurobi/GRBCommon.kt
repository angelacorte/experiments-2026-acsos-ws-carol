@file:Suppress("MatchingDeclarationName")

package it.unibo.collektive.solver.gurobi

import com.gurobi.gurobi.GRB
import com.gurobi.gurobi.GRBLinExpr
import com.gurobi.gurobi.GRBModel
import com.gurobi.gurobi.GRBQuadExpr
import com.gurobi.gurobi.GRBVar
import it.unibo.collektive.mathutils.zeroVec

/**
 * Wraps an array of Gurobi decision variables as a single vector.
 *
 * Provides dimension-independent access to the underlying variables and exposes
 * the vector's dimensionality via the [dimensions] property. Used to pass decision
 * variable vectors between QP model construction and objective/constraint builders.
 *
 * @property variables The array of Gurobi decision variables that make up this vector.
 * @property dimensions The number of variables (i.e., the dimension of the vector).
 */
class GRBVector(val variables: Array<GRBVar>) {
    val dimensions: Int get() = variables.size

    /**
     * Returns the scalar decision variable at [index].
     */
    operator fun get(index: Int): GRBVar = variables[index]
}

/**
 * Adds [dimension] continuous scalar variables to the model, each bounded in
 * `[lowerBound, upperBound]`, and wraps them in a [GRBVector].
 */
fun GRBModel.addVecVar(dimension: Int, lowerBound: Double, upperBound: Double, name: String): GRBVector =
    GRBVector(Array(dimension) { i -> addVar(lowerBound, upperBound, 0.0, GRB.CONTINUOUS, "$name[$i]") })

/**
 * Appends `ρ·‖u − a‖²` to this expression in expanded form:
 * `ρ·Σᵢ (uᵢ² − 2aᵢuᵢ + aᵢ²)`.
 *
 * @param u   decision-variable vector
 * @param a   constant vector (same length as [u])
 * @param rho non-negative weight
 */
fun GRBQuadExpr.addRhoNorm2Sq(u: GRBVector, a: DoubleArray, rho: Double = 1.0) {
    require(u.dimensions == a.size) { "u and a must have the same length" }
    for (i in u.variables.indices) {
        addTerm(rho, u[i], u[i]) // ρ·uᵢ²
        addTerm(-2.0 * rho * a[i], u[i]) // −2ρaᵢuᵢ
        addConstant(rho * a[i] * a[i]) // ρaᵢ²
    }
}

/**
 * Constructs the linear expression `multiplier · vectorᵀ · u`.
 *
 * This is the algebraic bridge between a gradient `∇h(p)` and the QP constraint
 * `∇h(p)ᵀ u ≥ …` under first-order dynamics `ṗ = u`.
 *
 * @receiver decision-variable vector `u`
 * @param vector constant coefficient vector (must have the same length as [this])
 * @param multiplier scalar pre-multiplier (default 1.0)
 */
fun GRBVector.toLinExpr(vector: DoubleArray, multiplier: Double = 1.0): GRBLinExpr {
    require(vector.size == dimensions) { "Dimension mismatch: |v|=${vector.size}, |u|=$dimensions" }
    return GRBLinExpr().also { expr ->
        for (i in vector.indices) expr.addTerm(multiplier * vector[i], this[i])
    }
}

/**
 * Constructs the quadratic expression `[coefficient] · ‖u‖²` (i.e. `‖u − 0‖²` scaled).
 */
fun GRBVector.toQuadExpr(coefficient: Double = 1.0): GRBQuadExpr =
    GRBQuadExpr().also { it.addRhoNorm2Sq(this, zeroVec(dimensions), coefficient) }
