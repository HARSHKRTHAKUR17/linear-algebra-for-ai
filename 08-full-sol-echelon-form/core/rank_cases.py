from core.rank import rank


def classify_rank(A):
    rows = len(A)
    cols = len(A[0])

    r = rank(A)

    return {
        "rows": rows,
        "cols": cols,
        "rank": r,
        "full_row_rank": r == rows,
        "full_column_rank": r == cols,
        "full_rank": r == min(rows, cols),
        "rank_deficient": r < min(rows, cols),
    }