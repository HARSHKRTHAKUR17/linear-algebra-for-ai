from core.matrix_space import (
    is_symmetric,
    is_upper_triangular,
    is_diagonal,
)


def test_symmetric_matrix():
    A = [
        [1, 2, 3],
        [2, 4, 5],
        [3, 5, 6],
    ]

    assert is_symmetric(A)


def test_non_symmetric_matrix():
    A = [
        [1, 2],
        [3, 4],
    ]

    assert not is_symmetric(A)


def test_upper_triangular():
    A = [
        [1, 2, 3],
        [0, 4, 5],
        [0, 0, 6],
    ]

    assert is_upper_triangular(A)


def test_not_upper_triangular():
    A = [
        [1, 2],
        [3, 4],
    ]

    assert not is_upper_triangular(A)


def test_diagonal():
    A = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3],
    ]

    assert is_diagonal(A)


def test_symmetric_upper_triangular_is_diagonal():
    A = [
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3],
    ]

    assert is_symmetric(A)
    assert is_upper_triangular(A)
    assert is_diagonal(A)