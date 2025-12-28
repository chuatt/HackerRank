"""
Problem: Alphabet Rangoli
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/alphabet-rangoli/problem

Summary:
Given an integer size (1 <= size < 27), print an alphabet rangoli of that size.
The rangoli uses lowercase letters, with '-' as padding.

Example (size = 5):
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

Approach:
1. The total width is (4 * size - 3).
2. For each row i from size-1 down to 0, build a sequence:
   letters[size-1 : i : -1] + letters[i : size]
3. Join letters with '-' and center to the total width using '-'.
4. Mirror the top half to form the bottom half.
"""

from __future__ import annotations

import string

def alphabet_rangoli(size: int) -> str:
    """
    Return the alphabet rangoli as a single string with newline separators.

    Args:
        size: Rangoli size (1 <= size < 27)

    Returns:
        Rangoli string with newline characters.
    """
    letters = string.ascii_lowercase
    width = 4 * size - 3

    lines: list[str] = []

    # Top half (including center line)
    for i in range(size - 1, -1, -1):
        left = letters[size - 1 : i : -1]
        right = letters[i:size]
        row = "-".join(left + right)
        lines.append(row.center(width, "-"))

    # Bottom half (mirror, excluding center line)
    lines.extend(lines[-2::-1])

    return "\n".join(lines)


def print_rangoli(size: int) -> None:
    """Print the alphabet rangoli (HackerRank expects printing)."""
    print(alphabet_rangoli(size))


if __name__ == "__main__":
    n = int(input().strip())
    print_rangoli(n)
    