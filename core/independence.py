from core.rank import rank


def is_independent(vectors):
    """
    Returns True if the given vectors are linearly independent.
    Each vector should be provided as a column.
    """

    if not vectors:
        return True

    rows = len(vectors[0])
    cols = len(vectors)

    matrix = [
        [vectors[j][i] for j in range(cols)]
        for i in range(rows)
    ]

    return rank(matrix) == cols


def is_dependent(vectors):
    return not is_independent(vectors)