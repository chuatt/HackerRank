"""
Problem: Mutations
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/python-mutations/problem

Summary:
Given a string, an index (position), and a character, replace the character at
the given index and return the updated string.

Example:
Input:
abracadabra
5 k

Output:
abrackdabra

Approach:
1. Convert the string to a list of characters (mutable).
2. Replace the element at the given index.
3. Join the list back into a string.

Constraints:
0 <= position < len(string)
"""


def mutate_string(s: str, position: int, character: str) -> str:
    """Return a copy of s with the character at 'position' replaced."""
    chars = list(s)
    chars[position] = character
    return "".join(chars)


if __name__ == "__main__":
    s = input().strip()
    position_str, character = input().split()
    position = int(position_str)

    print(mutate_string(s, position, character))
