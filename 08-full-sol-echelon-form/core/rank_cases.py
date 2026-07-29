from __future__ import annotations

import numpy as np

from .rank import rank


def rank_case(A: np.ndarray):

    rows, cols = A.shape

    r = rank(A)

    if r == rows == cols:
        return "Full Rank"

    if r == rows and rows < cols:
        return "Full Row Rank"

    if r == cols and cols < rows:
        return "Full Column Rank"

    return "Rank Deficient"