from __future__ import annotations

import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = np.asarray(data, dtype=float)

        if self.data.ndim != 2:
            raise ValueError("Matrix must be two-dimensional.")

    @property
    def shape(self):
        return self.data.shape

    @property
    def rows(self):
        return self.data.shape[0]

    @property
    def cols(self):
        return self.data.shape[1]