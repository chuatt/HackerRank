"""
Problem: Text Alignment
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/text-alignment/problem

Summary:
Given an odd integer `thickness`, print the HackerRank logo using text alignment
methods: ljust, center, and rjust.

The logo consists of:
1. Top cone
2. Top pillars
3. Middle belt
4. Bottom pillars
5. Bottom cone

Approach:
- Use string multiplication with alignment helpers:
  - ljust()
  - center()
  - rjust()
- Carefully control spacing based on the `thickness` value.

Constraints:
- thickness must be an odd number
- 0 < thickness < 50
"""


def print_hackerrank_logo(thickness: int) -> None:
    """Print the HackerRank logo with the given thickness."""
    h = "H"

    # Top cone
    for i in range(thickness):
        print((h * i).rjust(thickness - 1) + h + (h * i).ljust(thickness - 1))

    # Top pillars
    for _ in range(thickness + 1):
        print((h * thickness).center(thickness * 2) +
              (h * thickness).center(thickness * 6))

    # Middle belt
    for _ in range((thickness + 1) // 2):
        print((h * thickness * 5).center(thickness * 6))

    # Bottom pillars
    for _ in range(thickness + 1):
        print((h * thickness).center(thickness * 2) +
              (h * thickness).center(thickness * 6))

    # Bottom cone
    for i in range(thickness):
        print(
            ((h * (thickness - i - 1)).rjust(thickness) +
             h +
             (h * (thickness - i - 1)).ljust(thickness))
            .rjust(thickness * 6)
        )


if __name__ == "__main__":
    thickness = int(input().strip())
    print_hackerrank_logo(thickness)
