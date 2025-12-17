"""
Problem: String Validators
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/string-validators/problem

Summary:
Given a string, determine whether it contains:
1. Any alphanumeric characters
2. Any alphabetical characters
3. Any digits
4. Any lowercase characters
5. Any uppercase characters

Each result is printed on a new line as either True or False.

Example:
Input:
qA2

Output:
True
True
True
True
True

Approach:
1. Iterate through each character in the string.
2. Use Python built-in string methods:
   - isalnum()
   - isalpha()
   - isdigit()
   - islower()
   - isupper()
3. Use `any()` to check if at least one character satisfies each condition.

Constraints:
1 ≤ len(s) ≤ 1000
String contains only ASCII characters.
"""


def string_validators(s: str) -> list[bool]:
    """Return validation results for the given string."""
    return [
        any(c.isalnum() for c in s),
        any(c.isalpha() for c in s),
        any(c.isdigit() for c in s),
        any(c.islower() for c in s),
        any(c.isupper() for c in s),
    ]


if __name__ == "__main__":
    s = input().strip()

    results = string_validators(s)
    for value in results:
        print(value)
