import numpy as np

from linear_system import solve

A = np.array([
    [2, 1],
    [4, 3]
])

b = np.array([5, 11])

print(solve(A, b))