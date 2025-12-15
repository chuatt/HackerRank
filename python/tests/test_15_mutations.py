from python.algorithms.n15_mutations import mutate_string


def test_mutate_middle():
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"


def test_mutate_first_char():
    assert mutate_string("hello", 0, "H") == "Hello"


def test_mutate_last_char():
    assert mutate_string("hello", 4, "!") == "hell!"


def test_mutate_with_digit():
    assert mutate_string("abc", 1, "9") == "a9c"


def test_mutate_same_char_no_change():
    assert mutate_string("abc", 1, "b") == "abc"
