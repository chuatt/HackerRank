"""
Problem: String Split and Join
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/python-string-split-and-join/problem

Summary:
Given a string consisting of space-separated words, return a new string where
spaces are replaced by hyphens.

Example:
Input:  "this is a string"
Output: "this-is-a-string"

Approach:
1. Use str.split(" ") to break the string into a list of words.
2. Use "-".join(words) to reassemble them with hyphens.
3. Return the transformed string.

Constraints:
0 < len(line) ≤ 1000
"""


def split_and_join(line: str) -> str:
    """Return the input string with spaces replaced by hyphens."""
    words = line.split(" ")
    return "-".join(words)


if __name__ == "__main__":
    text = input().rstrip()
    print(split_and_join(text))
