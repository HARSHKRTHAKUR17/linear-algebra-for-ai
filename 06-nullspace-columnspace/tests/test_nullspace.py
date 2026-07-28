import numpy as np

from null_space import null_space


def test_nullspace():
    A = np.array([
        [1, 2],
        [2, 4]
    ])

    basis = null_space(A)

    assert basis.shape[0] == 1