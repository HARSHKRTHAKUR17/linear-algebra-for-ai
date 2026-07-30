from core.rref import rref
from core.pivots import get_pivot_columns, get_free_columns
from core.rank import rank


class CompleteSolution:
    def __init__(
        self,
        rref_matrix,
        pivot_columns,
        free_columns,
        particular_solution,
        general_solution,
        has_solution,
        unique_solution,
    ):
        self.rref = rref_matrix
        self.pivot_columns = pivot_columns
        self.free_columns = free_columns
        self.particular_solution = particular_solution
        self.general_solution = general_solution
        self.has_solution = has_solution
        self.unique_solution = unique_solution


def complete_solution(A, b):
    augmented = [row + [rhs] for row, rhs in zip(A, b)]
    r = rref(augmented)

    pivot_cols = get_pivot_columns(r)
    free_cols = get_free_columns(r)

    rows = len(A)
    cols = len(A[0])

    has_solution = True

    for row in r:
        if all(abs(x) < 1e-10 for x in row[:-1]) and abs(row[-1]) > 1e-10:
            has_solution = False
            break

    particular = [0] * cols

    if has_solution:
        for i, c in enumerate(pivot_cols):
            if c < cols:
                particular[c] = r[i][-1]

    general = {}

    for i, c in enumerate(pivot_cols):
        if c < cols:
            general[f"x{c+1}"] = {
                "constant": r[i][-1],
                "coefficients": {
                    f"x{j+1}": -r[i][j]
                    for j in free_cols
                },
            }

    return CompleteSolution(
        r,
        pivot_cols,
        free_cols,
        particular,
        general,
        has_solution,
        has_solution and len(free_cols) == 0,
    )