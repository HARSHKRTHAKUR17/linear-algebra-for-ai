"""
Utility functions for matrices.
"""

from __future__ import annotations

import numpy as np


def identity(
    size: int,
) -> np.ndarray:
    """
    Creates an identity matrix.
    """

    return np.eye(size)


def is_square(
    matrix: np.ndarray,
) -> bool:
    """
    Checks whether matrix is square.
    """

    return (
        matrix.ndim == 2
        and matrix.shape[0] == matrix.shape[1]
    )