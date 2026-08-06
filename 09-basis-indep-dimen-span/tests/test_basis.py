from core.basis import is_basis


def test_basis_r2():
    vectors = [
        [1, 0],
        [0, 1]
    ]

    assert is_basis(vectors)


def test_not_basis_dependent():
    vectors = [
        [1, 2],
        [2, 4]
    ]

    assert not is_basis(vectors)


def test_not_basis_insufficient_vectors():
    vectors = [
        [1, 0]
    ]

    assert not is_basis(vectors)


def test_basis_r3():
    vectors = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

    assert is_basis(vectors)