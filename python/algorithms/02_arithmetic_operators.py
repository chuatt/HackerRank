"""
Problem: Arithmetic Operators
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/python-arithmetic-operators

Summary:
Given two integers a and b, print three results on separate lines:
1. a + b
2. a - b
3. a * b

Approach:
Straightforward arithmetic operations following stdin → print pattern.

Constraints:
1 ≤ a ≤ 10^10
1 ≤ b ≤ 10^10

This file is formatted cleanly for learning, readability, and GitHub portfolio purposes.
"""

def arithmetic_operations(a: int, b: int) -> tuple[int, int, int]:
    """Return sum, difference, and product of two integers."""
    return a + b, a - b, a * b


if __name__ == "__main__":
    a = int(input())
    b = int(input())

    s, d, p = arithmetic_operations(a, b)

    print(s)
    print(d)
    print(p)
