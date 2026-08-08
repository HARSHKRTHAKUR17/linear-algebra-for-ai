from core.matrix_space import (
    is_symmetric,
    is_upper_triangular,
    is_diagonal,
)

from core.rank_one import (
    is_rank_one,
    outer_product,
)

from core.graph import (
    adjacency_matrix,
    degree,
    is_symmetric_graph,
)


# -----------------------------
# Matrix Spaces
# -----------------------------

A = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6],
]

print("Symmetric:", is_symmetric(A))
print("Upper triangular:", is_upper_triangular(A))
print("Diagonal:", is_diagonal(A))


# -----------------------------
# Rank 1
# -----------------------------

u = [1, 2, 3]
v = [4, 5]

A = outer_product(u, v)

print("\nRank-1 Matrix:")
for row in A:
    print(row)

print("Rank 1:", is_rank_one(A))


# -----------------------------
# Graph
# -----------------------------

edges = [
    (0, 1),
    (0, 2),
    (1, 2),
]

G = adjacency_matrix(
    num_nodes=3,
    edges=edges,
)

print("\nAdjacency Matrix:")

for row in G:
    print(row)

print("Symmetric:", is_symmetric_graph(G))
print("Degree of node 0:", degree(G, 0))