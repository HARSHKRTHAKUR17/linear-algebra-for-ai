from core.null_space import nullity


def test_nullity_identity():
    A = [
        [1, 0],
        [0, 1]
    ]

    assert nullity(A) == 0


def test_nullity_rank_deficient():
    A = [
        [1, 2],
        [2, 4]
    ]

    assert nullity(A) == 1


def test_nullity_rectangular():
    A = [
        [1, 2, 3],
        [0, 1, 4]
    ]

    assert nullity(A) == 1