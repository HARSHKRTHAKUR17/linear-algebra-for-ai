from __future__ import annotations

import numpy as np

from .rref import rref


def general_solution(A: np.ndarray, b: np.ndarray):
    augmented = np.column_stack((A, b))

    reduced, pivots = rref(augmented)

    return reduced, pivots