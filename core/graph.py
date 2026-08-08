def adjacency_matrix(num_nodes, edges, directed=False):
    """
    Construct an adjacency matrix from a list of edges.

    edges contains tuples of the form:
        (source, destination)

    Nodes are numbered from 0 to num_nodes - 1.
    """

    A = [
        [0 for _ in range(num_nodes)]
        for _ in range(num_nodes)
    ]

    for u, v in edges:
        A[u][v] = 1

        if not directed:
            A[v][u] = 1

    return A


def degree(A, node):
    """
    Return the degree of a node in an undirected graph.
    """

    return sum(A[node])


def is_symmetric_graph(A):
    """
    An undirected graph has a symmetric adjacency matrix.
    """

    rows = len(A)

    for i in range(rows):
        for j in range(rows):
            if A[i][j] != A[j][i]:
                return False

    return True