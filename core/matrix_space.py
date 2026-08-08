def is_symmetric(A):
    """
    Check whether a square matrix is symmetric.
    """

    rows = len(A)

    if rows == 0:
        return True

    if any(len(row) != rows for row in A):
        return False

    for i in range(rows):
        for j in range(i + 1, rows):
            if A[i][j] != A[j][i]:
                return False

    return True


def is_upper_triangular(A):
    """
    Check whether a square matrix is upper triangular.
    """

    rows = len(A)

    if rows == 0:
        return True

    if any(len(row) != rows for row in A):
        return False

    for i in range(rows):
        for j in range(i):
            if A[i][j] != 0:
                return False

    return True


def is_diagonal(A):
    """
    Check whether a square matrix is diagonal.
    """

    rows = len(A)

    if rows == 0:
        return True

    if any(len(row) != rows for row in A):
        return False

    for i in range(rows):
        for j in range(rows):
            if i != j and A[i][j] != 0:
                return False

    return True