from core.complete_solution import complete_solution
from core.rank_cases import classify_rank

A = [
    [1, 0, 2, -1],
    [0, 1, 3, 5]
]

b = [7, 4]

solution = complete_solution(A, b)

print("Particular Solution:")
print(solution.particular_solution)

print()

print("General Solution:")
print(solution.general_solution)

print()

print("Rank Classification:")
print(classify_rank(A))