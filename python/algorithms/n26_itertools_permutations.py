"""
Problem: itertools.permutations()

Platform: HackerRank

Link:
https://www.hackerrank.com/challenges/itertools-permutations/problem

Summary:
Given a string S and an integer k, print all possible permutations of
length k of the string in lexicographically sorted order.

Example:
Input:
HACK 2

Output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

Approach:
- Read the string S and integer k from stdin.
- Sort the characters of S to ensure lexicographic order.
- Use itertools.permutations to generate permutations of length k.
- Print each permutation on a separate line.
"""


from itertools import permutations


def solve() -> None:
    """
    Read input from stdin and print permutations line by line.
    """
    s, k = input().split()
    k = int(k)

    for perm in permutations(sorted(s), k):
        print("".join(perm))


if __name__ == "__main__":
    solve()
