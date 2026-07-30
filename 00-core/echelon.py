from __future__ import annotations

import numpy as np


def echelon_form(matrix: np.ndarray, tol: float = 1e-10):
    A = matrix.astype(float).copy()

    rows, cols = A.shape
    pivot_columns = []

    pivot_row = 0

    for col in range(cols):
        pivot = None

        for row in range(pivot_row, rows):
            if abs(A[row, col]) > tol:
                pivot = row
                break

        if pivot is None:
            continue

        if pivot != pivot_row:
            A[[pivot_row, pivot]] = A[[pivot, pivot_row]]

        for row in range(pivot_row + 1, rows):
            factor = A[row, col] / A[pivot_row, col]
            A[row] -= factor * A[pivot_row]

        pivot_columns.append(col)

        pivot_row += 1

        if pivot_row == rows:
            break

    A[np.abs(A) < tol] = 0

    return A, pivot_columns