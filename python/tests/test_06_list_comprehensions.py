from python.algorithms.n06_list_comprehensions import valid_coordinates


def test_small_example():
    x, y, z, n = 1, 1, 2, 3
    result = valid_coordinates(x, y, z, n)

    expected = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 0, 2],
        [0, 1, 0],
        [0, 1, 1],
        [0, 1, 2],
        [1, 0, 0],
        [1, 0, 1],
        [1, 0, 2],
        [1, 1, 0],
        [1, 1, 2],
    ]

    assert result == expected


def test_no_exclusions():
    # n is too large, so no coordinates sum to it
    x, y, z, n = 1, 1, 1, 100
    result = valid_coordinates(x, y, z, n)

    expected = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1],
    ]

    assert result == expected


def test_exclude_middle_values():
    x, y, z, n = 2, 2, 2, 3
    result = valid_coordinates(x, y, z, n)

    # brute-force recompute valid expected values
    expected = [
        [i, j, k]
        for i in range(3)
        for j in range(3)
        for k in range(3)
        if i + j + k != 3
    ]

    assert result == expected


def test_single_dimension_zero():
    x, y, z, n = 0, 1, 1, 1
    result = valid_coordinates(x, y, z, n)

    expected = [
        [0, 0, 0],
        [0, 0, 1],
        [0, 1, 0],
        [0, 1, 1],
    ]

    # Remove elements where sum == 1
    expected = [item for item in expected if sum(item) != 1]

    assert result == expected
