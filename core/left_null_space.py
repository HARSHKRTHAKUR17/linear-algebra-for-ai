from core.null_space import nullity


def left_nullity(A):
    """
    Returns the dimension of the left null space.
    """

    rows = len(A)

    from core.rank import rank

    return rows - rank(A)


def left_null_space_basis(A):
    """
    Implemented later using transpose.
    """

    raise NotImplementedError(
        "Implemented after transpose utilities."
    )