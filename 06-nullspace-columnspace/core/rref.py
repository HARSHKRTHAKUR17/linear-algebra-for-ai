from __future__ import annotations

import numpy as np


def rref(matrix, tol=1e-10):
    A = matrix.astype(float).copy()

    rows, cols = A.shape
    pivot_columns = []

    r = 0

    for c in range(cols):

        pivot = None

        for i in range(r, rows):
            if abs(A[i, c]) > tol:
                pivot = i
                break

        if pivot is None:
            continue

        A[[r, pivot]] = A[[pivot, r]]

        A[r] /= A[r, c]

        for i in range(rows):
            if i != r:
                A[i] -= A[i, c] * A[r]

        pivot_columns.append(c)

        r += 1

        if r == rows:
            break

    A[np.abs(A) < tol] = 0

    return A, pivot_columns