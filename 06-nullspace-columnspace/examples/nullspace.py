import numpy as np

from null_space import null_space

A = np.array([
    [1, 2, 3],
    [2, 4, 6]
])

print(null_space(A))