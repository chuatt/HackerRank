"""
Problem: Python Loops
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/python-loops

Summary:
Given an integer n, print the square of each non-negative integer i such that:
0 ≤ i < n

Example:
n = 3
Output:
0
1
4

Approach:
Use a simple for-loop over range(n) and print i*i for each iteration.

Constraints:
1 ≤ n ≤ 20

This file follows the same clean, consistent structure used across the repository.
"""

def squares_upto(n: int) -> list[int]:
    """Return a list of squares for all integers i where 0 ≤ i < n."""
    return [i * i for i in range(n)]


if __name__ == "__main__":
    n = int(input())

    for value in squares_upto(n):
        print(value)