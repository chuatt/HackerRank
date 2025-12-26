"""
Problem: Text Wrap
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/text-wrap/problem

Summary:
You are given a string and an integer max_width. Wrap the string so that each
line has exactly max_width characters (except possibly the last), and return
the wrapped result using newline characters ('\\n').

Example:
Input string: "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width: 4

Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

Approach:
Use Python's built-in `textwrap.fill()` to wrap long strings into fixed-width
lines. It will insert newline characters at the correct positions.

"""

from __future__ import annotations

import textwrap


def wrap(string: str, max_width: int) -> str:
    """Return the wrapped string using newline characters."""
    return textwrap.fill(string, width=max_width)


def wrap_text(string: str, max_width: int) -> str:
    """Alias for tests: same behavior as wrap()."""
    return wrap(string, max_width)


if __name__ == "__main__":
    s = input().rstrip("\n")
    width = int(input().strip())

    print(wrap(s, width))
