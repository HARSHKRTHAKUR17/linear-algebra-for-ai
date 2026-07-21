from typing import Tuple

import numpy as np


def compute_matrix_equation(
    coefficient_matrix: np.ndarray,
    variable_vector: np.ndarray,
) -> np.ndarray:
    
    return coefficient_matrix @ variable_vector


def main() -> None:
    A = np.array([
        [2, 1],
        [1, -1]
    ])

    X = np.array([
        [2],
        [1]
    ])

    B = compute_matrix_equation(A, X)

    print("Coefficient Matrix (A):")
    print(A)

    print("\nVariable Vector (X):")
    print(X)

    print("\nOutput Vector (B = AX):")
    print(B)


if __name__ == "__main__":
    main()