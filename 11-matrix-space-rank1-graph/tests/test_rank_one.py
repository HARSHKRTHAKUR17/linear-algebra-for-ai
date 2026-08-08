from core.rank_one import (
    is_rank_one,
    outer_product,
)


def test_rank_one_matrix():
    A = [
        [1, 2],
        [2, 4],
        [3, 6],
    ]

    assert is_rank_one(A)


def test_outer_product():
    u = [1, 2, 3]
    v = [4, 5]

    A = outer_product(u, v)

    assert A == [
        [4, 5],
        [8, 10],
        [12, 15],
    ]


def test_outer_product_is_rank_one():
    u = [1, 2, 3]
    v = [4, 5]

    A = outer_product(u, v)

    assert is_rank_one(A)