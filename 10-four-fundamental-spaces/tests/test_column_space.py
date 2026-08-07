from core.column_space import (
    column_space_basis,
    column_space_dimension,
)


def test_column_space_dimension_identity():
    A = [
        [1, 0],
        [0, 1]
    ]

    assert column_space_dimension(A) == 2


def test_column_space_basis_identity():
    A = [
        [1, 0],
        [0, 1]
    ]

    basis = column_space_basis(A)

    assert basis == [
        [1, 0],
        [0, 1]
    ]


def test_rank_deficient_column_space():
    A = [
        [1, 2],
        [2, 4]
    ]

    basis = column_space_basis(A)

    assert len(basis) == 1