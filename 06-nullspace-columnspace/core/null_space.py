from __future__ import annotations

import numpy as np

from rref import rref


def null_space(A):
    R, pivots = rref(A)

    rows, cols = R.shape

    free = [c for c in range(cols) if c not in pivots]

    basis = []

    for free_col in free:

        x = np.zeros(cols)

        x[free_col] = 1

        for row, pivot in enumerate(pivots):
            x[pivot] = -R[row, free_col]

        basis.append(x)

    return np.array(basis)