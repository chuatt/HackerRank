"""
Unit tests for n11_swap_case.py

Tests the swap_case(s) function to ensure:
- Lowercase → uppercase
- Uppercase → lowercase
- Digits and symbols remain unchanged
- Mixed cases transform correctly
- Edge cases (empty string, only symbols, long strings)
"""

from python.algorithms.n11_swap_case import swap_case


def test_basic_example():
    s = "HackerRank.com presents 'Pythonist 2'."
    expected = "hACKERrANK.COM PRESENTS 'pYTHONIST 2'."
    assert swap_case(s) == expected


def test_all_lowercase():
    assert swap_case("abc") == "ABC"


def test_all_uppercase():
    assert swap_case("XYZ") == "xyz"


def test_mixed_case():
    assert swap_case("AbC123") == "aBc123"


def test_symbols_unchanged():
    assert swap_case("!@#$%^&*()") == "!@#$%^&*()"


def test_empty_string():
    assert swap_case("") == ""


def test_long_string():
    s = "a" * 1000 + "B" * 1000
    expected = "A" * 1000 + "b" * 1000
    assert swap_case(s) == expected
