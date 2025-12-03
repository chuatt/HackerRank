"""
Problem: Write a Function (Leap Year)
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/write-a-function

Summary:
Determine whether a given year is a leap year in the Gregorian calendar.

Leap year rules:
1. The year is evenly divisible by 4
2. Except years divisible by 100 (not leap years)
3. Except years divisible by 400 (leap years)

Examples:
- 2000 → leap year   (divisible by 400)
- 1900 → not leap    (divisible by 100 but not 400)
- 1996 → leap year   (divisible by 4 and not 100)
- 1990 → not leap    (not divisible by 4)

Constraints:
1900 ≤ year ≤ 10^5

This file maintains the same clean structure and readability for GitHub portfolio purposes.
"""

def is_leap(year: int) -> bool:
    """Return True if the given year is a leap year, else False."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))
