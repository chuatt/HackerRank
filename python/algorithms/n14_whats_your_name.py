"""
Problem: What's Your Name?
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/whats-your-name/problem

Summary:
You are given a first name and a last name on separate lines.
Print a greeting message in the following format:

Hello firstname lastname! You just delved into python.

Example:
Input:
Ross
Taylor

Output:
Hello Ross Taylor! You just delved into python.

Approach:
1. Accept first name and last name as strings.
2. Format the output using an f-string.
3. Print the greeting exactly as required.

Constraints:
Length of first and last names ≤ 10.
"""


def print_full_name(first_name: str, last_name: str) -> None:
    """Print a greeting message using the provided first and last name."""
    print(f"Hello {first_name} {last_name}! You just delved into python.")


if __name__ == "__main__":
    first = input().strip()
    last = input().strip()
    print_full_name(first, last)
