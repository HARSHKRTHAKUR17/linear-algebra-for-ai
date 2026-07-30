from __future__ import annotations

import numpy as np

from .echelon import echelon_form


def rank(matrix: np.ndarray) -> int:
    _, pivots = echelon_form(matrix)
    return len(pivots)