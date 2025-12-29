"""
Tests for Alphabet Rangoli (HackerRank).

Module under test:
python.algorithms.n22_alphabet_rangoli

Function:
print_rangoli(size)
"""

from python.algorithms.n22_alphabet_rangoli import print_rangoli


def test_rangoli_size_3(capsys):
    """
    Test alphabet rangoli with size = 3.
    """
    print_rangoli(3)
    captured = capsys.readouterr().out

    expected = (
        "--c--\n"
        "-c-b-c-\n"
        "c-b-a-b-c\n"
        "-c-b-c-\n"
        "--c--\n"
    )

    assert captured == expected


def test_rangoli_size_5(capsys):
    """
    Test alphabet rangoli with size = 5.
    """
    print_rangoli(5)
    captured = capsys.readouterr().out

    expected = (
        "--------e--------\n"
        "------e-d-e------\n"
        "----e-d-c-d-e----\n"
        "--e-d-c-b-c-d-e--\n"
        "e-d-c-b-a-b-c-d-e\n"
        "--e-d-c-b-c-d-e--\n"
        "----e-d-c-d-e----\n"
        "------e-d-e------\n"
        "--------e--------\n"
    )

    assert captured == expected


def test_rangoli_min_size_1(capsys):
    """
    Edge case: minimum size.
    """
    print_rangoli(1)
    captured = capsys.readouterr().out

    expected = "a\n"

    assert captured == expected
