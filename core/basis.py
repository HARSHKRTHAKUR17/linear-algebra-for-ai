from core.independence import is_independent
from core.span import spans_space


from typing import List

def is_basis(vectors: List[List[float]]) -> bool:
    """
    Checks whether the vectors form a basis.
    """

    return (
        is_independent(vectors)
        and spans_space(vectors)
    )