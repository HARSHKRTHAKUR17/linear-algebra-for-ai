"""
Complete LU Solver
"""

from __future__ import annotations

import numpy as np

from backward_substitution import backward_substitution
from forward_substitution import forward_substitution
from lu_decomposition import lu_decomposition


def solve(
    matrix: np.ndarray,
    output_vector: np.ndarray,
):

    lower, upper = lu_decomposition(
        matrix
    )

    intermediate = forward_substitution(
        lower,
        output_vector,
    )

    solution = backward_substitution(
        upper,
        intermediate,
    )

    return solution


def main():

    matrix = np.array(
        [
            [2, 1, 1],
            [4, -6, 0],
            [-2, 7, 2],
        ]
    )

    output = np.array(
        [
            [5],
            [-2],
            [9],
        ]
    )

    solution = solve(
        matrix,
        output,
    )

    print(solution)

    assert np.allclose(
        matrix @ solution,
        output,
    )


if __name__ == "__main__":
    main()