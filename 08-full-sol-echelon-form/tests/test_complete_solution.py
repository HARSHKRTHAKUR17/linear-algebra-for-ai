from core.complete_solution import complete_solution


def test_unique_solution():
    A = [
        [1, 0],
        [0, 1]
    ]

    b = [3, 5]

    result = complete_solution(A, b)

    assert result.has_solution is True
    assert result.unique_solution is True
    assert result.free_columns == []
    assert result.particular_solution == [3, 5]


def test_infinite_solutions():
    A = [
        [1, 2, 3],
        [0, 0, 0]
    ]

    b = [4, 0]

    result = complete_solution(A, b)

    assert result.has_solution is True
    assert result.unique_solution is False
    assert len(result.free_columns) == 2


def test_no_solution():
    A = [
        [1, 1],
        [1, 1]
    ]

    b = [2, 3]

    result = complete_solution(A, b)

    assert result.has_solution is False


def test_particular_solution_exists():
    A = [
        [1, 0, 2],
        [0, 1, 3]
    ]

    b = [7, 4]

    result = complete_solution(A, b)

    assert result.particular_solution[0] == 7
    assert result.particular_solution[1] == 4