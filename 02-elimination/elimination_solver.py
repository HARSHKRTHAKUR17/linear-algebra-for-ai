"""
Lecture 02: Complete Gaussian Elimination Solver

Combines forward elimination and back substitution
to solve a system of linear equations.
"""

from __future__ import annotations

import numpy as np

from gaussian_elimination import forward_elimination
from back_substitution import back_substitution


def solve_linear_system(
    coefficient_matrix: np.ndarray,
    output_vector: np.ndarray,
) -> np.ndarray:
    """
    Solves Ax = b using Gaussian Elimination.
    """

    upper_matrix, modified_vector = forward_elimination(
        coefficient_matrix,
        output_vector,
    )

    solution = back_substitution(
        upper_matrix,
        modified_vector,
    )

    return solution


def verify_solution(
    coefficient_matrix: np.ndarray,
    output_vector: np.ndarray,
    solution: np.ndarray,
) -> None:
    """
    Verifies the computed solution.
    """

    computed_output = coefficient_matrix @ solution

    print("\nVerification (A @ x):")
    print(computed_output)

    print("\nOriginal b:")
    print(output_vector)

    assert np.allclose(
        computed_output,
        output_vector,
    ), "Verification failed."

    numpy_solution = np.linalg.solve(
        coefficient_matrix,
        output_vector,
    )

    assert np.allclose(
        solution,
        numpy_solution,
    ), "Solution differs from NumPy."

    print("\n✓ Solution verified successfully.")
    print("✓ Matches NumPy implementation.")


def main() -> None:

    coefficient_matrix = np.array(
        [
            [2, 1, 1],
            [4, -6, 0],
            [-2, 7, 2],
        ],
        dtype=float,
    )

    output_vector = np.array(
        [
            [5],
            [-2],
            [9],
        ],
        dtype=float,
    )

    solution = solve_linear_system(
        coefficient_matrix,
        output_vector,
    )

    print("Solution:")
    print(solution)

    verify_solution(
        coefficient_matrix,
        output_vector,
        solution,
    )


if __name__ == "__main__":
    main()