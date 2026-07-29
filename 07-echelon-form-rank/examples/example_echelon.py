import numpy as np

from core.echelon import echelon_form

A = np.array([
    [1, 2, 3],
    [2, 4, 7],
    [1, 1, 2]
])

E, pivots = echelon_form(A)

print("Echelon Form:")
print(E)

print("\nPivot Columns:", pivots)