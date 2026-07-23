"""
Lecture 03 Demo
"""

from __future__ import annotations

import numpy as np

from matrix_inverse import inverse
from matrix_multiplication import multiply


def main() -> None:

    matrix_a = np.array(
        [
            [2, 1],
            [5, 3],
        ],
        dtype=float,
    )

    matrix_b = np.array(
        [
            [4, 7],
            [1, 2],
        ],
        dtype=float,
    )

    print("A")
    print(matrix_a)

    print("\nB")
    print(matrix_b)

    print("\nA × B")
    print(
        multiply(
            matrix_a,
            matrix_b,
        )
    )

    print("\nInverse of A")
    print(
        inverse(
            matrix_a,
        )
    )


if __name__ == "__main__":
    main()