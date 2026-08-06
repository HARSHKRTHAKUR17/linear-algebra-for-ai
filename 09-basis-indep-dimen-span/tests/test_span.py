from core.span import (
    spans_space,
    span_dimension,
)


def test_span_r2():
    vectors = [
        [1, 0],
        [0, 1]
    ]

    assert spans_space(vectors)


def test_line_not_plane():
    vectors = [
        [1, 0]
    ]

    assert not spans_space(vectors)


def test_span_dimension():
    vectors = [
        [1, 0],
        [0, 1]
    ]

    assert span_dimension(vectors) == 2


def test_dependent_span():
    vectors = [
        [1, 2],
        [2, 4]
    ]

    assert span_dimension(vectors) == 1