import numpy as np

from core.rref import rref

A = np.array([
    [1, 2, 3],
    [2, 4, 7],
    [1, 1, 2]
])

R, pivots = rref(A)

print("Reduced Row Echelon Form:")
print(R)

print("\nPivot Columns:", pivots)