from __future__ import annotations

from typing import Sequence

import numpy as np

from vector import Vector


def linear_combination(
    vectors: Sequence[Vector],
    coefficients: Sequence[float],
) -> Vector:
    """
    Computes a linear combination of vectors.

    Example:
        2*v1 - 3*v2 + 4*v3
    """

    if len(vectors) == 0:
        raise ValueError("At least one vector is required.")

    if len(vectors) != len(coefficients):
        raise ValueError(
            "Number of vectors must equal number of coefficients."
        )

    dimension = vectors[0].dimension

    for vector in vectors:
        if vector.dimension != dimension:
            raise ValueError(
                "All vectors must have the same dimension."
            )

    result = np.zeros(dimension)

    for coefficient, vector in zip(coefficients, vectors):
        result += coefficient * vector.to_numpy()

    return Vector(result)


def coefficient_matrix(vectors: Sequence[Vector]) -> np.ndarray:
    """
    Builds a matrix whose columns are the given vectors.
    """

    if len(vectors) == 0:
        raise ValueError("Vector list cannot be empty.")

    dimension = vectors[0].dimension

    for vector in vectors:
        if vector.dimension != dimension:
            raise ValueError(
                "Vectors must have equal dimensions."
            )

    return np.column_stack(
        [vector.to_numpy() for vector in vectors]
    )


def solve_linear_combination(
    vectors: Sequence[Vector],
    target: Vector,
) -> np.ndarray:
    """
    Finds coefficients c such that

        c1*v1 + c2*v2 + ... = target

    if a solution exists.
    """

    matrix = coefficient_matrix(vectors)

    coefficients, residuals, rank, singular_values = np.linalg.lstsq(
        matrix,
        target.to_numpy(),
        rcond=None,
    )

    reconstruction = matrix @ coefficients

    if not np.allclose(reconstruction, target.to_numpy()):
        raise ValueError(
            "Target vector is not a linear combination of the given vectors."
        )

    return coefficients


def is_linear_combination(
    vectors: Sequence[Vector],
    target: Vector,
    tolerance: float = 1e-9,
) -> bool:
    """
    Returns True if target lies in the span of the vectors.
    """

    matrix = coefficient_matrix(vectors)

    coefficients, *_ = np.linalg.lstsq(
        matrix,
        target.to_numpy(),
        rcond=None,
    )

    reconstruction = matrix @ coefficients

    return np.allclose(
        reconstruction,
        target.to_numpy(),
        atol=tolerance,
    )


def reconstruct_vector(
    vectors: Sequence[Vector],
    coefficients: Sequence[float],
) -> Vector:
    """
    Alias for readability.
    """

    return linear_combination(vectors, coefficients)