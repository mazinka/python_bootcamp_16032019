from mathematica.algebra.matrices import add_matrices, add_matrices_v1, add_matrices_v2, sub_matrices

def test_add_matrices():

    a = [
    [1,2,3],
    [4,5,6]
    ]

    b = [
        [1, 1, 1],
        [1, 1, 1]
    ]

    result = [
        [2, 3, 4],
        [5, 6, 7]
    ]
    assert add_matrices(a,b) == result


def test_sub_matrices():

    a = [
    [1,2,3],
    [4,5,6]
    ]

    b = [
        [1, 1, 1],
        [1, 1, 1]
    ]

    result = [
        [0, 1, 2],
        [3, 4, 5]
    ]

    assert sub_matrices(a, b) == result

def test_add_matrices_v1():

    a = [
    [1,2,3],
    [4,5,6]
    ]

    b = [
        [1, 1, 1],
        [1, 1, 1]
    ]

    result = [
        [1, 1],[2,1]
        [3, 4, 5]
    ]

    assert sub_matrices(a, b) == result


def add_test_add_matrices_v2(a,b):
    return [[el_a + el_b for el_a, el_b in zip(row_A, row_b)] for row_A, row_b in zip(a,b)]



def test_sub_matrices():

    a = [
    [1,2,3],
    [4,5,6]
    ]

    b = [
        [1, 1, 1],
        [1, 1, 1]
    ]

    result = [
        [0, 1, 2],
        [3, 4, 5]
    ]

    assert sub_matrices(a, b) == result