import numpy as np

from column_space import column_space


def test_columnspace():
    A = np.array([
        [1, 2],
        [2, 4]
    ])

    C = column_space(A)

    assert C.shape[1] == 1