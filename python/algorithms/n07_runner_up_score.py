"""
Problem: Find the Runner-Up Score!
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Summary:
You are given an integer n and then a list of n integers. The goal is to print
the second highest unique score (the "runner-up" score).

Example:
Input:  2 3 6 6 5
Unique sorted values → [2, 3, 5, 6]
Runner-up → 5

Approach:
1. Convert the list to a set to remove duplicates.
2. Sort the unique values.
3. Return the second largest value (index -2).

Constraints:
2 ≤ n ≤ 10
-100 ≤ A[i] ≤ 100
"""


def runner_up_score(values: list[int]) -> int:
    """Return the second highest unique integer from the list."""
    unique_sorted = sorted(set(values))
    return unique_sorted[-2]


if __name__ == "__main__":
    _ = int(input().strip())
    arr = list(map(int, input().split()))
    print(runner_up_score(arr))
