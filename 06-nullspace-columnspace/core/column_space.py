from __future__ import annotations

import numpy as np

from .rref import rref


def column_space(A):
    _, pivots = rref(A)

    return A[:, pivots]