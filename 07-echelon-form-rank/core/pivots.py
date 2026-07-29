from __future__ import annotations

import numpy as np

from .echelon import echelon_form


def pivot_columns(matrix: np.ndarray):
    _, pivots = echelon_form(matrix)
    return pivots


def pivot_rows(matrix: np.ndarray):
    echelon, _ = echelon_form(matrix)

    rows = []

    for i, row in enumerate(echelon):
        if np.any(np.abs(row) > 1e-10):
            rows.append(i)

    return rows


def free_columns(matrix: np.ndarray):
    _, pivots = echelon_form(matrix)

    return [i for i in range(matrix.shape[1]) if i not in pivots]