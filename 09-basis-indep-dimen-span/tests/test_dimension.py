from core.dimension import dimension


def test_dimension_r2():
    vectors = [
        [1, 0],
        [0, 1]
    ]

    assert dimension(vectors) == 2


def test_dimension_line():
    vectors = [
        [1, 0]
    ]

    assert dimension(vectors) == 1


def test_dimension_dependent():
    vectors = [
        [1, 2],
        [2, 4]
    ]

    assert dimension(vectors) == 1


def test_dimension_r3():
    vectors = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    assert dimension(vectors) == 3