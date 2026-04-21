package it.unibo.collektive.mathutils

/**
 * Performs component-wise subtraction between two constant vectors.
 *
 * This operator is used to compute relative positions or differences between vectors.
 *
 * @receiver the minuend constant vector
 * @param other the subtrahend constant vector
 * @return a new constant vector representing the component-wise difference
 */
operator fun DoubleArray.minus(other: DoubleArray): DoubleArray = DoubleArray(size) { i -> this[i] - other[i] }

/**
 * Dot product between two constant vectors.
 */
operator fun DoubleArray.times(other: DoubleArray): Double {
    require(this.size == other.size) { "Dimension mismatch: expected ${this.size}, got ${other.size}" }
    return DoubleArray(size) { i -> this[i] * other[i] }.sum()
}

/**
 * Scalar times vector multiplication.
 */
operator fun Double.times(other: DoubleArray): DoubleArray = DoubleArray(other.size) { i -> this * other[i] }

/**
 * Computes the squared Euclidean norm of a constant vector.
 *
 * This function is typically used in Control Lyapunov Function (CLF) or Control Barrier Function (CBF) scalar terms.
 *
 * @receiver the constant vector
 * @return the squared norm value
 */
fun DoubleArray.squaredNorm(): Double = sumOf { it * it } // v^Tv

/**
 * Creates a constant zero vector of the given dimension.
 *
 * This utility is typically used to represent static entities
 * (e.g., obstacles with zero velocity).
 */
fun zeroVec(dim: Int): DoubleArray = DoubleArray(dim) { 0.0 }
