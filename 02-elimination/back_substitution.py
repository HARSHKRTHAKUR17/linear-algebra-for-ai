"""
Lecture 02: Back Substitution

Solves an upper triangular system produced by
Gaussian Elimination.
"""

from __future__ import annotations

import numpy as np


def validate_inputs(
    upper_matrix: np.ndarray,
    output_vector: np.ndarray,
) -> None:
    """
    Validates the dimensions of the input matrices.
    """

    if upper_matrix.ndim != 2:
        raise ValueError("Coefficient matrix must be two-dimensional.")

    if output_vector.ndim != 2:
        raise ValueError("Output vector must be two-dimensional.")

    rows, columns = upper_matrix.shape

    if rows != columns:
        raise ValueError("Coefficient matrix must be square.")

    if output_vector.shape != (rows, 1):
        raise ValueError(
            "Output vector must have shape (n, 1)."
        )


def back_substitution(
    upper_matrix: np.ndarray,
    output_vector: np.ndarray,
) -> np.ndarray:
    """
    Solves an upper triangular system using
    back substitution.
    """

    validate_inputs(
        upper_matrix,
        output_vector,
    )

    number_of_rows = upper_matrix.shape[0]

    solution = np.zeros(
        (number_of_rows, 1),
        dtype=float,
    )

    for row in range(
        number_of_rows - 1,
        -1,
        -1,
    ):

        if np.isclose(
            upper_matrix[row, row],
            0.0,
        ):
            raise ValueError(
                "Matrix is singular. No unique solution exists."
            )

        known_value = np.dot(
            upper_matrix[row, row + 1 :],
            solution[row + 1 :],
        )

        solution[row] = (
            output_vector[row] - known_value
        ) / upper_matrix[row, row]

    return solution


def main() -> None:

    upper_matrix = np.array(
        [
            [2, 1, -1],
            [0, 3, 2],
            [0, 0, 4],
        ]
    )

    output_vector = np.array(
        [
            [8],
            [13],
            [12],
        ]
    )

    solution = back_substitution(
        upper_matrix,
        output_vector,
    )

    print("Solution Vector:")
    print(solution)


if __name__ == "__main__":
    main()