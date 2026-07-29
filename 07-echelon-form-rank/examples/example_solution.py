import numpy as np

from core.solution import general_solution

A = np.array([
    [1, 2, 1],
    [2, 4, 2]
])

b = np.array([
    3,
    6
])

R, pivots = general_solution(A, b)

print("Reduced Augmented Matrix:")
print(R)

print("\nPivot Columns:", pivots)