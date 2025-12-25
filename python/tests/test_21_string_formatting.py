"""
Tests for HackerRank problem: String Formatting

Validates:
- Correct decimal, octal, hex (uppercase), binary output
- Right-justified formatting
- Correct width based on binary(n)
- No trailing spaces
"""

from python.algorithms.n21_string_formatting import print_formatted


def test_string_formatting_sample_input(capsys):
    """
    Sample test from HackerRank (n = 17).
    """
    print_formatted(17)
    captured = capsys.readouterr().out

    expected = (
        "    1     1     1     1\n"
        "    2     2     2    10\n"
        "    3     3     3    11\n"
        "    4     4     4   100\n"
        "    5     5     5   101\n"
        "    6     6     6   110\n"
        "    7     7     7   111\n"
        "    8    10     8  1000\n"
        "    9    11     9  1001\n"
        "   10    12     A  1010\n"
        "   11    13     B  1011\n"
        "   12    14     C  1100\n"
        "   13    15     D  1101\n"
        "   14    16     E  1110\n"
        "   15    17     F  1111\n"
        "   16    20    10 10000\n"
        "   17    21    11 10001\n"
    )

    assert captured == expected


def test_string_formatting_minimum(capsys):
    """
    Edge case: smallest valid input.
    """
    print_formatted(1)
    captured = capsys.readouterr().out

    expected = "1 1 1 1\n"
    assert captured == expected


def test_string_formatting_hex_uppercase(capsys):
    """
    Ensure hexadecimal output is uppercase.
    """
    print_formatted(15)
    captured = capsys.readouterr().out

    assert "A" in captured
    assert "B" in captured
    assert "C" in captured
    assert "D" in captured
    assert "E" in captured
    assert "F" in captured


def test_string_formatting_no_trailing_spaces(capsys):
    """
    Ensure no trailing whitespace on any line.
    """
    print_formatted(10)
    captured = capsys.readouterr().out

    for line in captured.splitlines():
        assert line == line.rstrip()
