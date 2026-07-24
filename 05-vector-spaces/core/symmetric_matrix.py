from __future__ import annotations

import numpy as np


def is_symmetric(matrix: np.ndarray) -> bool:
    """
    Returns True if A = A^T.
    """

    matrix = np.asarray(matrix, dtype=float)

    if matrix.shape[0] != matrix.shape[1]:
        return False

    return np.allclose(
        matrix,
        matrix.T,
    )


def transpose(matrix: np.ndarray) -> np.ndarray:
    """
    Returns the transpose of a matrix.
    """

    return np.asarray(matrix).T


def print_matrix_info(matrix: np.ndarray) -> None:
    """
    Displays basic information.
    """

    print("=" * 40)
    print("MATRIX INFORMATION")
    print("=" * 40)

    print(matrix)

    print()

    print("Transpose:\n")
    print(matrix.T)

    print()

    print(f"Symmetric: {is_symmetric(matrix)}")