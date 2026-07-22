"""
Lecture 02: Gaussian Elimination

Performs forward elimination to transform a system of
linear equations into an upper triangular matrix.
"""

from __future__ import annotations

import numpy as np


def validate_inputs(
    coefficient_matrix: np.ndarray,
    output_vector: np.ndarray,
) -> None:
    """
    Validates the dimensions of the input matrices.
    """

    if coefficient_matrix.ndim != 2:
        raise ValueError("Coefficient matrix must be two-dimensional.")

    if output_vector.ndim != 2:
        raise ValueError("Output vector must be two-dimensional.")

    rows, columns = coefficient_matrix.shape

    if rows != columns:
        raise ValueError("Coefficient matrix must be square.")

    if output_vector.shape != (rows, 1):
        raise ValueError(
            "Output vector must have shape (n, 1)."
        )


def forward_elimination(
    coefficient_matrix: np.ndarray,
    output_vector: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Performs Gaussian Elimination with partial pivoting.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Upper triangular matrix and modified output vector.
    """

    validate_inputs(
        coefficient_matrix,
        output_vector,
    )

    matrix = coefficient_matrix.astype(float).copy()
    vector = output_vector.astype(float).copy()

    number_of_rows = matrix.shape[0]

    for pivot_index in range(number_of_rows):

        # Partial Pivoting
        largest_row = pivot_index + np.argmax(
            np.abs(
                matrix[pivot_index:, pivot_index]
            )
        )

        if np.isclose(
            matrix[largest_row, pivot_index],
            0.0,
        ):
            raise ValueError(
                "Matrix is singular. No unique solution exists."
            )

        if largest_row != pivot_index:
            matrix[[pivot_index, largest_row]] = (
                matrix[[largest_row, pivot_index]]
            )

            vector[[pivot_index, largest_row]] = (
                vector[[largest_row, pivot_index]]
            )

        pivot = matrix[pivot_index, pivot_index]

        for row in range(
            pivot_index + 1,
            number_of_rows,
        ):

            multiplier = (
                matrix[row, pivot_index] / pivot
            )

            matrix[row, pivot_index:] -= (
                multiplier
                * matrix[pivot_index, pivot_index:]
            )

            vector[row] -= (
                multiplier
                * vector[pivot_index]
            )

    return matrix, vector


def main() -> None:

    coefficient_matrix = np.array(
        [
            [2, 1, 1],
            [4, -6, 0],
            [-2, 7, 2],
        ]
    )

    output_vector = np.array(
        [
            [5],
            [-2],
            [9],
        ]
    )

    upper_matrix, modified_vector = forward_elimination(
        coefficient_matrix,
        output_vector,
    )

    print("Upper Triangular Matrix:")
    print(upper_matrix)

    print("\nModified Output Vector:")
    print(modified_vector)


if __name__ == "__main__":
    main()