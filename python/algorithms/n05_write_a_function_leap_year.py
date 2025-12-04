"""
Problem: Write a Function (Leap Year)
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/write-a-function/problem

Summary:
A year is a leap year if:
- It is divisible by 4
  - except divisible by 100
    - unless also divisible by 400

Approach:
Apply the Gregorian leap-year rules in order:
1. Check divisible by 400
2. Check divisible by 100
3. Check divisible by 4

Constraints:
1900 ≤ year ≤ 10^5
"""


def is_leap(year: int) -> bool:
    """Return True if the given year is a leap year."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    year_value = int(input().strip())
    print(is_leap(year_value))
