"""
Problem: itertools.product()

Platform: HackerRank

Link:
https://www.hackerrank.com/challenges/itertools-product/problem

Summary:
Given two lists A and B, compute and print their Cartesian product A × B
using itertools.product. The output must be printed as tuples in a single
line, separated by spaces, in sorted order.

Example:
Input:
1 2
3 4

Output:
(1, 3) (1, 4) (2, 3) (2, 4)

Approach:
- Read two lines of input and convert them into integer lists.
- Use itertools.product to generate the Cartesian product.
- Print each tuple separated by a space, exactly matching HackerRank's
  expected format.
"""

from itertools import product


def solve() -> None:
    """
    Read input from stdin and print the Cartesian product of two lists.
    """
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = product(a, b)
    print(" ".join(str(item) for item in result))


if __name__ == "__main__":
    solve()
