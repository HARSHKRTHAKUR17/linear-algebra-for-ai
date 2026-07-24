from __future__ import annotations

import numpy as np

from vector import Vector


def column_space(matrix: np.ndarray) -> list[Vector]:
    """
    Returns the columns of a matrix
    as Vector objects.
    """

    matrix = np.asarray(matrix, dtype=float)

    return [
        Vector(matrix[:, i])
        for i in range(matrix.shape[1])
    ]


def column_rank(matrix: np.ndarray) -> int:
    """
    Returns the rank of the column space.
    """

    matrix = np.asarray(matrix, dtype=float)

    return int(np.linalg.matrix_rank(matrix))


def print_column_space(matrix: np.ndarray) -> None:
    """
    Prints the column vectors.
    """

    columns = column_space(matrix)

    print("=" * 40)
    print("COLUMN SPACE")
    print("=" * 40)

    for i, column in enumerate(columns, start=1):
        print(f"Column {i}: {column}")

    print(f"\nRank: {column_rank(matrix)}")