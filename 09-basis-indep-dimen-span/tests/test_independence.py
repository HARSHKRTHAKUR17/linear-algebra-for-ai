from core.independence import (
    is_independent,
    is_dependent,
)


def test_independent_vectors():
    vectors = [
        [1, 0],
        [0, 1]
    ]

    assert is_independent(vectors)


def test_dependent_vectors():
    vectors = [
        [1, 2],
        [2, 4]
    ]

    assert is_dependent(vectors)


def test_standard_basis_r3():
    vectors = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    assert is_independent(vectors)


def test_four_vectors_r3():
    vectors = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]
    ]

    assert is_dependent(vectors)