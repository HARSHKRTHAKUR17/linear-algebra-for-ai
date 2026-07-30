from core.rank_cases import classify_rank


def test_full_column_rank():
    A = [
        [1, 0],
        [0, 1],
        [1, 1]
    ]

    result = classify_rank(A)

    assert result["full_column_rank"] is True
    assert result["full_row_rank"] is False
    assert result["full_rank"] is True


def test_full_row_rank():
    A = [
        [1, 2, 3],
        [0, 1, 4]
    ]

    result = classify_rank(A)

    assert result["full_row_rank"] is True
    assert result["full_column_rank"] is False
    assert result["full_rank"] is True


def test_square_full_rank():
    A = [
        [1, 0],
        [0, 1]
    ]

    result = classify_rank(A)

    assert result["full_rank"] is True
    assert result["rank"] == 2


def test_rank_deficient():
    A = [
        [1, 2],
        [2, 4]
    ]

    result = classify_rank(A)

    assert result["rank_deficient"] is True
    assert result["rank"] == 1