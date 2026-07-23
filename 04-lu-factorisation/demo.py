"""
LU Demonstration
"""

from __future__ import annotations

import numpy as np

from lu_decomposition import lu_decomposition


def main():

    matrix = np.array(
        [
            [2, 1],
            [6, 8],
        ]
    )

    L, U = lu_decomposition(matrix)

    print("Original")

    print(matrix)

    print()

    print("L")

    print(L)

    print()

    print("U")

    print(U)

    print()

    print("L @ U")

    print(L @ U)


if __name__ == "__main__":
    main()