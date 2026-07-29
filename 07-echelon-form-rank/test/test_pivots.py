import numpy as np

from core.pivots import pivot_columns, free_columns


def test_pivots():

    A = np.array([
        [1, 2],
        [2, 4]
    ])

    assert pivot_columns(A) == [0]
    assert free_columns(A) == [1]