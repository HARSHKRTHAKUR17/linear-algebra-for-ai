import numpy as np

from core.rank import rank

A = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
])

print("Rank =", rank(A))