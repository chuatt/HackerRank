"""
Problem: Python Division
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/python-division

Summary:
Given two integers a and b, print:
1. The result of integer division a // b
2. The result of float division a / b

No rounding or formatting is required.

Example:
a = 3, b = 5
- Integer division: 3 // 5 = 0
- Float division:   3 / 5 = 0.6

Approach:
Use Python's // operator for integer division and / for float division.

Constraints:
1 ≤ a ≤ 10^10
1 ≤ b ≤ 10^10

This file is formatted for readability and consistency with the repository structure.
"""

def division_results(a: int, b: int) -> tuple[int, float]:
    """Return integer division and float division of a by b."""
    return a // b, a / b


if __name__ == "__main__":
    a = int(input())
    b = int(input())

    int_div, float_div = division_results(a, b)

    print(int_div)
    print(float_div)
