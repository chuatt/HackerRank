"""
Problem: Capitalize!
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

Summary:
Given a string containing alphanumeric characters and spaces, capitalize the first
character of each word while preserving all spaces exactly as-is.

Example:
Input:  "  chris   alan  "
Output: "  Chris   Alan  "

Approach:
Scan the string character-by-character.
Capitalize a character if it is alphabetic AND either:
- it is the first character of the string, or
- the previous character is a space.
All other characters are kept unchanged, which preserves spacing and ensures
alphanumeric words like "12abc" remain "12abc".
"""


def solve(s):
    """
    Print the capitalized version of string s (spaces preserved).

    Args:
        s (str): Input string containing alphanumeric characters and spaces.
    """
    if not s:
        print()
        return

    out_chars = []
    prev_is_space = True

    for ch in s:
        if prev_is_space and ch.isalpha():
            out_chars.append(ch.upper())
        else:
            out_chars.append(ch)
        prev_is_space = (ch == " ")

    print("".join(out_chars))
