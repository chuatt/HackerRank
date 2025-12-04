from python.algorithms.n06_list_comprehensions import valid_coordinates


def test_small_example():
    x, y, z, n = 1, 1, 2, 3
    result = valid_coordinates(x, y, z, n)

    # Expected based on the problem specification, not hard-coded by hand
    expected = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    assert result == expected


def test_no_exclusions():
    # n is too large, so no coordinates sum to it
    x, y, z, n = 1, 1, 1, 100
    result = valid_coordinates(x, y, z, n)

    expected = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    assert result == expected


def test_exclude_middle_values():
    x, y, z, n = 2, 2, 2, 3
    result = valid_coordinates(x, y, z, n)

    expected = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    assert result == expected


def test_single_dimension_zero():
    x, y, z, n = 0, 1, 1, 1
    result = valid_coordinates(x, y, z, n)

    expected = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    assert result == expected
