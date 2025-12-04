"""
Use Ctrl + I to generate code

Problem: Python Loops
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/python-loops/problem

Summary:
Given an integer n, print i² for all non-negative integers i < n.

Approach:
Loop from 0 to n-1 and print the square of each number.

Constraints:
1 ≤ n ≤ 20
"""


def squares_upto(n: int) -> list[int]:
    """Return a list of square values from 0 to n-1."""
    return [i * i for i in range(n)]


if __name__ == "__main__":
    n_value = int(input().strip())

    for result in squares_upto(n_value):
        print(result)
