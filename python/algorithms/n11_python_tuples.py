"""
Problem: Tuples
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/python-tuples/problem

Summary:
Given an integer n and a list of n space-separated integers, create a tuple t.
Then compute and print the result of hash(t).

Example:
Input:
2
1 2
Tuple = (1, 2)
Output = hash((1, 2))

Approach:
1. Read integer n.
2. Read n integers and convert them into a tuple.
3. Use the built-in hash() function and print the result.

Constraints:
2 ≤ n ≤ 10
−100 ≤ integers ≤ 100
"""


def tuple_hash(values: list[int]) -> int:
    """Return the hash of the list of integers by converting it to a tuple."""
    return hash(tuple(values))


if __name__ == "__main__":
    n = int(input().strip())
    numbers = list(map(int, input().split()))
    print(tuple_hash(numbers))
