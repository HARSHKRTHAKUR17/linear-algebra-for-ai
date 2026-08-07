from core.four_fundamental_spaces import summary


def test_identity_matrix():
    A = [
        [1, 0],
        [0, 1]
    ]

    result = summary(A)

    assert result["rank"] == 2
    assert result["column_space_dimension"] == 2
    assert result["row_space_dimension"] == 2
    assert result["null_space_dimension"] == 0
    assert result["left_null_space_dimension"] == 0


def test_rank_deficient_matrix():
    A = [
        [1, 2],
        [2, 4]
    ]

    result = summary(A)

    assert result["rank"] == 1
    assert result["column_space_dimension"] == 1
    assert result["row_space_dimension"] == 1
    assert result["null_space_dimension"] == 1
    assert result["left_null_space_dimension"] == 1


def test_rectangular_matrix():
    A = [
        [1, 2, 3],
        [0, 1, 4]
    ]

    result = summary(A)

    assert result["rank"] == 2
    assert result["column_space_dimension"] == 2
    assert result["row_space_dimension"] == 2
    assert result["null_space_dimension"] == 1
    assert result["left_null_space_dimension"] == 0