from __future__ import annotations

import numpy as np

from .rref import rref


def complete_solution(A: np.ndarray, b: np.ndarray, tol: float = 1e-10):
    augmented = np.column_stack((A, b))

    R, pivots = rref(augmented)

    rows, cols = A.shape

    pivot_columns = [c for c in pivots if c < cols]

    free_columns = [c for c in range(cols) if c not in pivot_columns]

    inconsistent = False

    for row in R:
        if np.all(np.abs(row[:-1]) < tol) and abs(row[-1]) > tol:
            inconsistent = True
            break

    return {
        "rref": R,
        "pivot_columns": pivot_columns,
        "free_columns": free_columns,
        "has_solution": not inconsistent,
        "unique_solution": len(free_columns) == 0 and not inconsistent,
        "infinite_solutions": len(free_columns) > 0 and not inconsistent,
    }