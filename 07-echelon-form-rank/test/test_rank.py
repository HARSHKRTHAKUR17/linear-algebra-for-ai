import numpy as np

from core.rank import rank


def test_rank():
    A = np.eye(4)

    assert rank(A) == 4