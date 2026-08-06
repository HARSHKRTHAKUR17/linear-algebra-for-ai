from core.rank import rank


def span_dimension(vectors):
    """
    Returns the dimension of the span of the vectors.
    """

    if not vectors:
        return 0

    rows = len(vectors[0])
    cols = len(vectors)

    matrix = [
        [vectors[j][i] for j in range(cols)]
        for i in range(rows)
    ]

    return rank(matrix)


def spans_space(vectors):
    """
    Checks whether the vectors span R^n.
    """

    if not vectors:
        return False

    rows = len(vectors[0])

    return span_dimension(vectors) == rows