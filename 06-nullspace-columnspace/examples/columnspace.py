import numpy as np

from core.column_space import column_space

A = np.array([
    [1, 2, 3],
    [2, 4, 6]
])

print(column_space(A))