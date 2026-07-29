import numpy as np

from core.solution import general_solution


def test_solution():

    A = np.array([
        [1, 2],
        [2, 4]
    ])

    b = np.array([
        3,
        6
    ])

    R, _ = general_solution(A, b)

    assert R.shape == (2, 3)