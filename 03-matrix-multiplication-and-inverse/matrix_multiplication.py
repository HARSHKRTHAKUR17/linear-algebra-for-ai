"""
Lecture 03: Matrix Multiplication

Implements matrix multiplication from scratch.
"""

from __future__ import annotations

import numpy as np


def validate_dimensions(
    left_matrix: np.ndarray,
    right_matrix: np.ndarray,
) -> None:
    """
    Ensures matrix multiplication is valid.
    """

    if left_matrix.ndim != 2 or right_matrix.ndim != 2:
        raise ValueError("Both inputs must be two-dimensional matrices.")

    if left_matrix.shape[1] != right_matrix.shape[0]:
        raise ValueError(
            "Number of columns of first matrix "
            "must equal number of rows of second matrix."
        )


def multiply(
    left_matrix: np.ndarray,
    right_matrix: np.ndarray,
) -> np.ndarray:
    """
    Multiplies two matrices without using
    NumPy's matrix multiplication.
    """

    validate_dimensions(
        left_matrix,
        right_matrix,
    )

    rows = left_matrix.shape[0]
    columns = right_matrix.shape[1]
    common_dimension = left_matrix.shape[1]

    result = np.zeros(
        (rows, columns),
        dtype=float,
    )

    for row in range(rows):
        for column in range(columns):

            value = 0.0

            for index in range(common_dimension):

                value += (
                    left_matrix[row, index]
                    * right_matrix[index, column]
                )

            result[row, column] = value

    return result


def verify_result(
    left_matrix: np.ndarray,
    right_matrix: np.ndarray,
    result: np.ndarray,
) -> None:

    numpy_result = left_matrix @ right_matrix

    assert np.allclose(
        result,
        numpy_result,
    ), "Matrix multiplication failed."

    print("✓ Verification successful.")
    print("✓ Matches NumPy.")


def main() -> None:

    matrix_a = np.array(
        [
            [1, 2],
            [3, 4],
        ],
        dtype=float,
    )

    matrix_b = np.array(
        [
            [5, 6],
            [7, 8],
        ],
        dtype=float,
    )

    product = multiply(
        matrix_a,
        matrix_b,
    )

    print(product)

    verify_result(
        matrix_a,
        matrix_b,
        product,
    )


if __name__ == "__main__":
    main()