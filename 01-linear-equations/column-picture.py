"""
Lecture 01: Column Picture

Demonstrates that AX is a weighted combination
of the columns of A.
"""

import numpy as np


def compute_column_picture(
    coefficient_matrix: np.ndarray,
    variable_vector: np.ndarray,
) -> np.ndarray:
    """
    Computes AX using the column picture.
    """
    result = np.zeros(
        (coefficient_matrix.shape[0], 1)
    )

    for column_index in range(coefficient_matrix.shape[1]):
        column = coefficient_matrix[:, column_index].reshape(-1, 1)
        weight = variable_vector[column_index, 0]

        result += weight * column

    return result


def main() -> None:
    coefficient_matrix = np.array(
        [
            [2, 1],
            [1, -1],
        ]
    )

    variable_vector = np.array(
        [
            [2],
            [1],
        ]
    )

    column_picture_result = compute_column_picture(
        coefficient_matrix,
        variable_vector,
    )

    matrix_multiplication_result = (
        coefficient_matrix @ variable_vector
    )

    print("Column Picture Result:")
    print(column_picture_result)

    print("\nMatrix Multiplication Result:")
    print(matrix_multiplication_result)

    print("\nResults Match:")
    print(
        np.array_equal(
            column_picture_result,
            matrix_multiplication_result,
        )
    )


if __name__ == "__main__":
    main()