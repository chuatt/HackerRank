from python.algorithms.n02_arithmetic_operators import arithmetic_operations


def test_basic_operations():
    assert arithmetic_operations(3, 5) == (8, -2, 15)


def test_large_numbers():
    assert arithmetic_operations(10, 10) == (20, 0, 100)
