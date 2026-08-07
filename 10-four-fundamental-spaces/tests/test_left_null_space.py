from core.left_null_space import left_nullity


def test_left_nullity_identity():
    A = [
        [1, 0],
        [0, 1]
    ]

    assert left_nullity(A) == 0


def test_left_nullity_rectangular():
    A = [
        [1, 2],
        [0, 1],
        [1, 3]
    ]

    assert left_nullity(A) == 1


def test_left_nullity_rank_deficient():
    A = [
        [1, 2],
        [2, 4],
        [3, 6]
    ]

    assert left_nullity(A) == 2