"""
Unit tests for n13_split_and_join.py

Tests the split_and_join(line) function to ensure:
- Spaces are replaced by hyphens
- Multiple words handled correctly
- Leading/trailing/multiple spaces are handled as in Python's split(" ")
"""

from python.algorithms.n13_split_and_join import split_and_join


def test_basic_example():
    line = "this is a string"
    expected = "this-is-a-string"
    assert split_and_join(line) == expected


def test_single_word():
    line = "hello"
    expected = "hello"
    assert split_and_join(line) == expected


def test_multiple_spaces_between_words():
    # split(" ") keeps empty strings between consecutive spaces
    line = "this  has   extra spaces"
    expected = "this--has---extra-spaces"
    assert split_and_join(line) == expected


def test_leading_and_trailing_spaces():
    line = "  leading and trailing  "
    # Leading and trailing spaces become leading/trailing hyphens
    expected = "--leading-and-trailing--"
    assert split_and_join(line) == expected


def test_empty_string():
    # Edge case: split(" ") on "" returns ['']
    line = ""
    expected = ""
    assert split_and_join(line) == expected
