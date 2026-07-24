from __future__ import annotations

from typing import Sequence

import numpy as np

from vector import Vector
from linear_combination import coefficient_matrix


def is_subspace(vectors: Sequence[Vector]) -> bool:
    """
    Determines whether the supplied vectors define a subspace.

    Since every span of vectors is a subspace,
    any collection of vectors is treated as the generators
    of a subspace.
    """
    return len(vectors) > 0


def dimension(vectors: Sequence[Vector]) -> int:
    """
    Returns the dimension of the subspace
    spanned by the vectors.
    """

    if len(vectors) == 0:
        return 0

    matrix = coefficient_matrix(vectors)

    return int(np.linalg.matrix_rank(matrix))


def contains(
    vectors: Sequence[Vector],
    target: Vector,
) -> bool:
    """
    Checks whether the target vector belongs
    to the subspace.
    """

    if len(vectors) == 0:
        return target.is_zero()

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