import numpy as np

from core.vector import Vector
from core.linear_combination import (
    linear_combination,
    spans_vector,
)
from core.subspace import (
    contains,
    dimension,
)
from core.column_space import (
    print_column_space,
)
from core.symmetric_matrix import (
    print_matrix_info,
)


def main():

    print("=" * 60)
    print("VECTOR")
    print("=" * 60)

    v1 = Vector([1, 2])
    v2 = Vector([3, 4])

    print(v1)
    print(v2)

    print(v1 + v2)
    print(v1 - v2)

    print(v1.dot(v2))
    print(v1.norm())

    print()

    print("=" * 60)
    print("LINEAR COMBINATION")
    print("=" * 60)

    result = linear_combination(
        [v1, v2],
        [2, -1],
    )

    print(result)

    target = Vector([-1, 0])

    print(
        spans_vector(
            [v1, v2],
            target,
        )
    )

    print()

    print("=" * 60)
    print("SUBSPACE")
    print("=" * 60)

    print(
        dimension([v1, v2])
    )

    print(
        contains(
            [v1, v2],
            target,
        )
    )

    print()

    print("=" * 60)
    print("COLUMN SPACE")
    print("=" * 60)

    A = np.array(
        [
            [1, 2],
            [3, 4],
            [5, 6],
        ]
    )

    print_column_space(A)

    print()

    print("=" * 60)
    print("SYMMETRIC MATRIX")
    print("=" * 60)

    S = np.array(
        [
            [1, 2, 3],
            [2, 5, 6],
            [3, 6, 9],
        ]
    )

    print_matrix_info(S)


if __name__ == "__main__":
    main()