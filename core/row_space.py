from core.rref import rref


def row_space_basis(A):
    """
    Returns the non-zero rows of the RREF,
    which form a basis of the row space.
    """

    R = rref(A)

    basis = []

    for row in R:
        if any(abs(x) > 1e-10 for x in row):
            basis.append(row)

    return basis