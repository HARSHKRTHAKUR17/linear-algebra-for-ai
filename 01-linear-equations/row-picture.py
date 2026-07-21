"""
Lecture 01: Row Picture

Solves a system of linear equations
using NumPy.
"""

import numpy as np


def solve_linear_system(
    coefficient_matrix: np.ndarray,
    output_vector: np.ndarray,
) -> np.ndarray:
    """
    Solves AX = B.
    """
    return np.linalg.solve(
        coefficient_matrix,
        output_vector,
    )


def verify_solution(
    coefficient_matrix: np.ndarray,
    solution_vector: np.ndarray,
    output_vector: np.ndarray,
) -> bool:
    """
    Verifies that AX equals B.
    """
    calculated_output = (
        coefficient_matrix @ solution_vector
    )

    return np.allclose(
        calculated_output,
        output_vector,
    )


def main() -> None:
    coefficient_matrix = np.array(
        [
            [2, 1],
            [1, -1],
        ]
    )

    output_vector = np.array(
        [
            [5],
            [1],
        ]
    )

    solution_vector = solve_linear_system(
        coefficient_matrix,
        output_vector,
    )

    print("Solution Vector (X):")
    print(solution_vector)

    print("\nVerification:")
    print(
        verify_solution(
            coefficient_matrix,
            solution_vector,
            output_vector,
        )
    )


if __name__ == "__main__":
    main()