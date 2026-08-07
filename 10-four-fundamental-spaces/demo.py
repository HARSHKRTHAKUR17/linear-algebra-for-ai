from core.column_space import (
    column_space_basis,
    column_space_dimension,
)

from core.row_space import (
    row_space_basis,
    row_space_dimension,
)

from core.null_space import (
    nullity,
)

from core.left_null_space import (
    left_nullity,
)

from core.four_fundamental_spaces import (
    summary,
)


def main():

    A = [
        [1, 2, 3],
        [2, 4, 6],
        [1, 1, 1]
    ]

    print("=" * 60)
    print("FOUR FUNDAMENTAL SUBSPACES")
    print("=" * 60)

    print("\nMatrix:")
    for row in A:
        print(row)

    print("\nSummary")
    print("-" * 60)

    info = summary(A)

    for key, value in info.items():
        print(f"{key:30}: {value}")

    print("\nColumn Space")
    print("-" * 60)

    print("Dimension:", column_space_dimension(A))
    print("Basis:")

    for vector in column_space_basis(A):
        print(vector)

    print("\nRow Space")
    print("-" * 60)

    print("Dimension:", row_space_dimension(A))
    print("Basis:")

    for vector in row_space_basis(A):
        print(vector)

    print("\nNull Space")
    print("-" * 60)

    print("Dimension:", nullity(A))

    print("\nLeft Null Space")
    print("-" * 60)

    print("Dimension:", left_nullity(A))


if __name__ == "__main__":
    main()