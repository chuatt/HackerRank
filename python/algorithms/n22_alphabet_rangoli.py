"""
n22_alphabet_rangoli.py

Problem: Alphabet Rangoli
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/alphabet-rangoli/problem

Summary:
Given an integer N (0 < N < 27), print an alphabet rangoli of size N.
The center uses 'a', and the boundary uses the Nth letter.

Approach:
1. Build the top half lines from the largest letter down to 'a'.
2. Mirror those lines to form the bottom half.
3. Each line is hyphen-centered to a fixed width: 4*N - 3.
"""


from __future__ import annotations


def build_rangoli(size: int) -> str:
    """
    Return the rangoli as a single string with newline separators.
    """
    if size <= 0 or size >= 27:
        return ""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3
    lines: list[str] = []

    # Top half (including middle)
    for i in range(size):
        left = alphabet[size - 1 : size - 1 - i : -1]  # descending
        right = alphabet[size - i - 1 : size]          # ascending
        seq = left + right
        line = "-".join(seq).center(width, "-")
        lines.append(line)

    # Bottom half (mirror, excluding middle)
    lines.extend(reversed(lines[:-1]))

    return "\n".join(lines)


def print_rangoli(size: int) -> None:
    """
    Print the rangoli (HackerRank expects printing).
    """
    result = build_rangoli(size)
    if result:
        print(result)


if __name__ == "__main__":
    n = int(input().strip())
    print_rangoli(n)
