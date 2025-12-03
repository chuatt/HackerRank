"""
Problem: Python If-Else
Platform: HackerRank
Link: https://www.hackerrank.com/challenges/py-if-else

Summary:
Given an integer n:
- If n is odd → print "Weird"
- If n is even and in the range 2–5 → print "Not Weird"
- If n is even and in the range 6–20 → print "Weird"
- If n is even and > 20 → print "Not Weird"

Approach:
Use conditional checks based on the rules above.

Constraints:
1 ≤ n ≤ 100

This file is written in a clean, modular structure for GitLab portfolio or testing.
"""

def weird_or_not(n: int) -> str:
    """Return whether n is Weird or Not Weird based on rules."""
    if n % 2 != 0:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"


if __name__ == "__main__":
    n = int(input().strip())
    print(weird_or_not(n))
