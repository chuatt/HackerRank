"""
Problem: String Formatting
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/python-string-formatting/problem

Summary:
Given an integer n, print the decimal, octal, hexadecimal (uppercase),
and binary representations of all numbers from 1 to n.
Each value must be right-aligned to the width of the binary representation of n.

Example:
Input:
17

Output:
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101

Approach:
1. Determine the width using the length of bin(n).
2. Loop from 1 to n.
3. Format each number using decimal, octal, hex (uppercase), and binary.
4. Right-align each value to the calculated width.

Constraints:
1 ≤ n ≤ 99
"""


def print_formatted(number: int) -> None:
    """Print formatted number representations from 1 to number."""
    width = len(bin(number)) - 2

    for i in range(1, number + 1):
        dec = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)

        print(f"{dec} {octal} {hexa} {binary}")


if __name__ == "__main__":
    n = int(input().strip())
    print_formatted(n)
