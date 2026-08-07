from core.rank import rank
from core.null_space import nullity
from core.left_null_space import left_nullity


def summary(A):
    rows = len(A)
    cols = len(A[0])

    r = rank(A)

    return {
        "rows": rows,
        "cols": cols,
        "rank": r,
        "column_space_dimension": r,
        "row_space_dimension": r,
        "null_space_dimension": nullity(A),
        "left_null_space_dimension": left_nullity(A),
    }