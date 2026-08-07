from core.rref import rref
from core.pivots import get_pivot_columns


def column_space_basis(A):
    """
    Returns the pivot columns of the ORIGINAL matrix,
    which form a basis of the column space.
    """

    R = rref(A)

    pivots = get_pivot_columns(R)

    basis = []

    for col in pivots:
        basis.append([row[col] for row in A])

    return basis