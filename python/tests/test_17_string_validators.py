from python.algorithms.n17_string_validators import string_validators


def test_mixed_characters():
    s = "qA2"
    result = string_validators(s)

    assert result == [
        True,   # alphanumeric
        True,   # alphabetic
        True,   # digit
        True,   # lowercase
        True,   # uppercase
    ]


def test_all_lowercase_letters():
    s = "hello"
    result = string_validators(s)

    assert result == [
        True,
        True,
        False,
        True,
        False,
    ]


def test_all_digits():
    s = "12345"
    result = string_validators(s)

    assert result == [
        True,
        False,
        True,
        False,
        False,
    ]


def test_uppercase_only():
    s = "ABC"
    result = string_validators(s)

    assert result == [
        True,
        True,
        False,
        False,
        True,
    ]


def test_special_characters_only():
    s = "!@#$%"
    result = string_validators(s)

    assert result == [
        False,
        False,
        False,
        False,
        False,
    ]
