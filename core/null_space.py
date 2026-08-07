from core.rref import rref
from core.pivots import (
    get_pivot_columns,
    get_free_columns,
)


def nullity(A):
    """
    Returns the dimension of the null space.
    """

    cols = len(A[0])

    pivots = get_pivot_columns(rref(A))

    return cols - len(pivots)


def null_space_basis(A):
    """
    Returns a basis for the null space.

    (Implementation will become more sophisticated
    after later lectures.)
    """

    raise NotImplementedError(
        "Will be fully implemented after Null Space lecture."
    )