from core.independence import is_independent
from core.span import spans_space


def is_basis(vectors):
    """
    Checks whether the vectors form a basis.
    """

    return (
        is_independent(vectors)
        and spans_space(vectors)
    )