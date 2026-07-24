from __future__ import annotations

from typing import Sequence

import numpy as np

from vector import Vector


def linear_combination(
    vectors: Sequence[Vector],
    coefficients: Sequence[float],
) -> Vector:
    """
    Computes

    c1*v1 + c2*v2 + ... + cn*vn
    """

    if len(vectors) == 0:
        raise ValueError("Vector list cannot be empty.")

    if len(vectors) != len(coefficients):
        raise ValueError(
            "Vectors and coefficients must have equal length."
        )

    dimension = vectors[0].dimension

    result = np.zeros(dimension)

    for coefficient, vector in zip(coefficients, vectors):

        if vector.dimension != dimension:
            raise ValueError(
                "All vectors must have equal dimension."
            )

        result += coefficient * vector.to_numpy()

    return Vector(result)


def coefficient_matrix(
    vectors: Sequence[Vector],
) -> np.ndarray:
    """
    Builds a matrix whose columns are the vectors.
    """

    if len(vectors) == 0:
        raise ValueError("Vector list cannot be empty.")

    return np.column_stack(
        [vector.to_numpy() for vector in vectors]
    )


def spans_vector(
    vectors: Sequence[Vector],
    target: Vector,
) -> bool:
    """
    Returns True if target is a linear combination
    of the supplied vectors.
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
    )


def solve_coefficients(
    vectors: Sequence[Vector],
    target: Vector,
) -> np.ndarray:
    """
    Finds coefficients satisfying

    Ax = b
    """

    matrix = coefficient_matrix(vectors)

    coefficients, *_ = np.linalg.lstsq(
        matrix,
        target.to_numpy(),
        rcond=None,
    )

    return coefficients