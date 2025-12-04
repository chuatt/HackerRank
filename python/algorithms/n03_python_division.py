"""
Problem: Python Division
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/python-division/problem

Summary:
Given two integers a and b:
- Print integer division (a // b)
- Print float division (a / b)

No rounding or formatting is necessary.

Approach:
Use Python's integer and float division operators.

Constraints:
1 ≤ a ≤ 10^10
1 ≤ b ≤ 10^10
"""


def division_results(a: int, b: int) -> tuple[int, float]:
    """Return integer and float division results."""
    return a // b, a / b


if __name__ == "__main__":
    a_value = int(input().strip())
    b_value = int(input().strip())

    int_div, float_div = division_results(a_value, b_value)

    print(int_div)
    print(float_div)
