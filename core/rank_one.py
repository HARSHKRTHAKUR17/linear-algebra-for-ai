from core.rank import rank


def is_rank_one(A):
    """
    Return True if A has rank exactly 1.
    """

    return rank(A) == 1

def outer_product(u, v):
    """
    Compute the outer product uv^T.

    u: column vector
    v: column vector
    """

    return [
        [u_i * v_j for v_j in v]
        for u_i in u
    ]