"""
LU Decomposition

A = LU
"""

from __future__ import annotations

import numpy as np


def lu_decomposition(
    matrix: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:

    matrix = matrix.astype(float)

    n = matrix.shape[0]

    lower = np.eye(n)

    upper = matrix.copy()

    for pivot in range(n):

        for row in range(
            pivot + 1,
            n,
        ):

            multiplier = (
                upper[row, pivot]
                / upper[pivot, pivot]
            )

            lower[row, pivot] = multiplier

            upper[row] -= (
                multiplier
                * upper[pivot]
            )

    return lower, upper


def main():

    matrix = np.array(
        [
            [2, 1, 1],
            [4, -6, 0],
            [-2, 7, 2],
        ]
    )

    L, U = lu_decomposition(matrix)

    print("L")
    print(L)

    print()

    print("U")
    print(U)


if __name__ == "__main__":
    main()