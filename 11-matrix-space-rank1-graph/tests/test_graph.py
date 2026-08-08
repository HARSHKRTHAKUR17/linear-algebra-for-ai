from core.graph import (
    adjacency_matrix,
    degree,
    is_symmetric_graph,
)


def test_undirected_graph():
    edges = [
        (0, 1),
        (0, 2),
        (1, 2),
    ]

    A = adjacency_matrix(
        num_nodes=3,
        edges=edges,
    )

    assert A == [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0],
    ]


def test_undirected_graph_is_symmetric():
    edges = [
        (0, 1),
        (1, 2),
    ]

    A = adjacency_matrix(
        num_nodes=3,
        edges=edges,
    )

    assert is_symmetric_graph(A)


def test_degree():
    edges = [
        (0, 1),
        (0, 2),
    ]

    A = adjacency_matrix(
        num_nodes=3,
        edges=edges,
    )

    assert degree(A, 0) == 2