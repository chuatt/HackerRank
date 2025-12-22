"""
Problem: Designer Door Mat
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/designer-door-mat/problem

Summary:
You are given the dimensions of a door mat. The mat must be symmetric,
contain the word 'WELCOME' at its center, and use only '.', '|', and '-'
characters. The width is always three times the height.

Approach:
1. Print the top half of the mat using increasing '.|.' patterns.
2. Print 'WELCOME' centered in the middle row.
3. Print the bottom half by mirroring the top half in reverse order.
4. Use str.center(width, '-') for correct alignment.

Constraints:
- N is an odd natural number.
- M = 3 * N
- Only '.', '|', and '-' characters are allowed.
"""


def print_designer_door_mat(n: int, m: int) -> None:
    """Print the Designer Door Mat pattern."""
    # Top half
    for i in range(n // 2):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(m, "-"))

    # Middle
    print("WELCOME".center(m, "-"))

    # Bottom half
    for i in range(n // 2 - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(m, "-"))


if __name__ == "__main__":
    n, m = map(int, input().split())
    print_designer_door_mat(n, m)
