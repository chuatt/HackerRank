"""
Tests for HackerRank - Alphabet Rangoli (n22).
"""

from python.algorithms.n22_alphabet_rangoli import print_rangoli


def test_rangoli_size_3(capsys):
    print_rangoli(3)
    captured = capsys.readouterr().out

    expected = (
        "----c----\n"
        "--c-b-c--\n"
        "c-b-a-b-c\n"
        "--c-b-c--\n"
        "----c----\n"
    )
    assert captured == expected


def test_rangoli_size_5(capsys):
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
