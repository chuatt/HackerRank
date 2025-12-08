from python.algorithms.n10_python_lists import process_commands


def test_sample_case():
    commands = [
        "insert 0 5",
        "insert 1 10",
        "insert 0 6",
        "print",
        "remove 6",
        "append 9",
        "append 1",
        "sort",
        "print",
        "pop",
        "reverse",
        "print",
    ]

    result = process_commands(commands)

    assert result == [
        [6, 5, 10],
        [1, 5, 9, 10],
        [9, 5, 1],
    ]


def test_only_appends_and_prints():
    commands = [
        "append 1",
        "append 2",
        "append 3",
        "print",
    ]

    result = process_commands(commands)

    assert result == [[1, 2, 3]]


def test_insert_and_remove():
    commands = [
        "append 1",
        "append 2",
        "append 3",
        "insert 1 99",  # [1, 99, 2, 3]
        "remove 2",     # [1, 99, 3]
        "print",
    ]

    result = process_commands(commands)

    assert result == [[1, 99, 3]]


def test_sort_and_reverse():
    commands = [
        "append 3",
        "append 1",
        "append 2",
        "sort",
        "print",
        "reverse",
        "print",
    ]

    result = process_commands(commands)

    assert result == [
        [1, 2, 3],
        [3, 2, 1],
    ]


def test_multiple_prints_without_modification():
    commands = [
        "append 4",
        "append 5",
        "print",
        "print",
    ]

    result = process_commands(commands)

    assert result == [
        [4, 5],
        [4, 5],
    ]
