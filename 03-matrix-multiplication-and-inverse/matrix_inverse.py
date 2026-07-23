"""
Lecture 03

Matrix inverse using Gauss-Jordan Elimination.
"""

from __future__ import annotations

import numpy as np

from matrix_utils import is_square


def inverse(
    matrix: np.ndarray,
) -> np.ndarray:

    if not is_square(matrix):
        raise ValueError(
            "Matrix must be square."
        )

    size = matrix.shape[0]

    augmented = np.hstack(
        (
            matrix.astype(float),
            np.eye(size),
        )
    )

    for pivot in range(size):

        largest = pivot + np.argmax(
            np.abs(
                augmented[pivot:, pivot]
            )
        )

        if np.isclose(
            augmented[largest, pivot],
            0,
        ):
            raise ValueError(
                "Matrix is singular."
            )

        augmented[[pivot, largest]] = (
            augmented[[largest, pivot]]
        )

        augmented[pivot] /= (
            augmented[pivot, pivot]
        )

        for row in range(size):

            if row == pivot:
                continue

            multiplier = augmented[
                row,
                pivot,
            ]

            augmented[row] -= (
                multiplier
                * augmented[pivot]
            )

    return augmented[:, size:]


def main() -> None:

    matrix = np.array(
        [
            [2, 1],
            [5, 3],
        ]
    )

    inverse_matrix = inverse(
        matrix,
    )

    print(inverse_matrix)

    print("\nVerification")

    print(
        matrix @ inverse_matrix
    )

    assert np.allclose(
        matrix @ inverse_matrix,
        np.eye(2),
    )


if __name__ == "__main__":
    main()