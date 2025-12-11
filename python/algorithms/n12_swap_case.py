"""
Problem: sWAP cASE
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/swap-case/problem

Summary:
Given a string s, return a new string where all lowercase letters become
uppercase, and all uppercase letters become lowercase. Non-alphabetic
characters remain unchanged.

Example:
Input:  "HackerRank.com presents 'Pythonist 2'."
Output: "hACKERrANK.COM PRESENTS 'pYTHONIST 2'."

Approach:
1. Iterate through each character.
2. If the character is lowercase → convert to uppercase.
3. If the character is uppercase → convert to lowercase.
4. Otherwise, keep the character unchanged.
5. Build and return the transformed string.

Constraints:
0 < len(s) ≤ 1000
"""


def swap_case(s: str) -> str:
    """Return a copy of s with swapped upper/lowercase characters."""
    result = []
    for char in s:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    text = input().rstrip()
    print(swap_case(text))
