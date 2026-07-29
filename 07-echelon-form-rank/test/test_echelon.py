import numpy as np

from core.echelon import echelon_form


def test_echelon():

    A = np.array([
        [1, 2],
        [2, 4]
    ])

    E, pivots = echelon_form(A)

    assert pivots == [0]