"""
Problem: Text Alignment
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/text-alignment/problem

Summary:
You are given partial code that generates the HackerRank logo of variable
thickness. The thickness must be an odd number. The goal is to print the logo
using the string methods: rjust, ljust, and center.

Approach:
Build the logo in 5 parts:
1. Top cone
2. Top pillars
3. Middle belt
4. Bottom pillars
5. Bottom cone
"""


def print_hackerrank_logo(thickness: int, char: str = "H") -> None:
    """Print the HackerRank logo with the given odd thickness."""
    t = thickness
    c = char

    # Top Cone
    for i in range(t):
        line = (c * i).rjust(t - 1) + c + (c * i).ljust(t - 1)
        print(line)

    # Top Pillars
    for _ in range(t + 1):
        line = (c * t).center(t * 2) + (c * t).center(t * 6)
        print(line)

    # Middle Belt
    for _ in range((t + 1) // 2):
        line = (c * (t * 5)).center(t * 6)
        print(line)

    # Bottom Pillars
    for _ in range(t + 1):
        line = (c * t).center(t * 2) + (c * t).center(t * 6)
        print(line)

    # Bottom Cone
    for i in range(t):
        line = ((c * (t - i - 1)).rjust(t) + c + (c * (t - i - 1)).ljust(t)).rjust(
            t * 6
        )
        print(line)


if __name__ == "__main__":
    thickness_value = int(input().strip())
    print_hackerrank_logo(thickness_value)
