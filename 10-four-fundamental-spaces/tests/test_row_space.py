from core.row_space import (
    row_space_basis,
    row_space_dimension,
)


def test_row_space_dimension_identity():
    A = [
        [1, 0],
        [0, 1]
    ]

    assert row_space_dimension(A) == 2


def test_row_space_basis_identity():
    A = [
        [1, 0],
        [0, 1]
    ]

    basis = row_space_basis(A)

    assert len(basis) == 2


def test_rank_deficient_row_space():
    A = [
        [1, 2],
        [2, 4]
    ]

    basis = row_space_basis(A)

    assert len(basis) == 1