import numpy as np

from rref import rref


def test_rref():

    A = np.array([
        [1, 2],
        [3, 4]
    ])

    R, _ = rref(A)

    expected = np.eye(2)

    assert np.allclose(R, expected)