"""
Problem: List Comprehensions
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/list-comprehensions/problem

Summary:
Given integers x, y, z and n representing the dimensions of a 3D grid and a
target sum n, generate all coordinates [i, j, k] such that:
- 0 <= i <= x
- 0 <= j <= y
- 0 <= k <= z
- i + j + k != n

The result should be printed as a list in lexicographic order.

Approach:
Use a nested list comprehension over the ranges 0..x, 0..y, 0..z and filter
out coordinates where i + j + k == n.
"""


def valid_coordinates(x: int, y: int, z: int, n: int) -> list[list[int]]:
    """Return all [i, j, k] where i + j + k != n within the given ranges."""
    return [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]


if __name__ == "__main__":
    x_val = int(input().strip())
    y_val = int(input().strip())
    z_val = int(input().strip())
    n_val = int(input().strip())

    print(valid_coordinates(x_val, y_val, z_val, n_val))
