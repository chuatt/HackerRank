from python.algorithms.n11_python_tuples import tuple_hash


def test_matches_builtin_hash_simple():
    values = [1, 2]
    assert tuple_hash(values) == hash(tuple(values))


def test_matches_builtin_hash_longer():
    values = [1, 2, 3, 4, 5]
    assert tuple_hash(values) == hash(tuple(values))


def test_negative_values():
    values = [-10, 0, 10]
    assert tuple_hash(values) == hash(tuple(values))


def test_duplicate_values():
    values = [5, 5, 5, 5]
    assert tuple_hash(values) == hash(tuple(values))


def test_order_matters():
    values1 = [1, 2, 3]
    values2 = [3, 2, 1]

    # Hashes should be different when order is different
    assert tuple_hash(values1) != tuple_hash(values2)
