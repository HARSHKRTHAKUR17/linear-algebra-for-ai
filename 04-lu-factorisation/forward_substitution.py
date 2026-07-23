"""
Forward Substitution

Solves Ly = b
where L is lower triangular.
"""

from __future__ import annotations

import numpy as np


def forward_substitution(
    lower_matrix: np.ndarray,
    output_vector: np.ndarray,
) -> np.ndarray:

    n = lower_matrix.shape[0]

    solution = np.zeros(
        (n, 1),
        dtype=float,
    )

    for row in range(n):

        known = np.dot(
            lower_matrix[row, :row],
            solution[:row],
        )

        solution[row] = (
            output_vector[row] - known
        ) / lower_matrix[row, row]

    return solution