# python/algorithms/n23_capitalize.py
"""
Problem: Capitalize!

Platform: HackerRank

Link:
https://www.hackerrank.com/challenges/capitalize/problem

Summary:
Given a full name string S containing alphanumeric characters and spaces, capitalize
the first character of each word while preserving all original spacing and leaving
the rest of each word unchanged.

Example:
Input:
alison heck
Output:
Alison Heck

Approach:
Walk through the string character-by-character. If a character is at the start of
the string or immediately follows a space, convert it to uppercase; otherwise keep
it unchanged. This preserves multiple spaces exactly and matches the rule that only
the first character of each word is capitalized.
"""


def solve(s: str) -> None:
    """
    Print the capitalized version of s, preserving spacing exactly.
    """
    if not s:
        print("")
        return

    chars = []
    for i, ch in enumerate(s):
        if i == 0 or s[i - 1] == " ":
            chars.append(ch.upper())
        else:
            chars.append(ch)

    print("".join(chars))


if __name__ == "__main__":
    solve(input())
