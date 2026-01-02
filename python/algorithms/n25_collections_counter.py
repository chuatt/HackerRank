"""
Problem: collections.Counter()

Platform: HackerRank

Link:
https://www.hackerrank.com/challenges/collections-counter/problem

Summary:
Raghu owns a shoe shop with a limited inventory of shoe sizes.
Each customer wants to buy a shoe of a specific size and is willing
to pay a given price only if that size is available.
Each shoe can be sold at most once.

Compute the total money earned by Raghu.

Example:
Input:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Output:
200

Approach:
- Count shoe sizes using collections.Counter.
- For each customer:
  - If the requested size is available, add the price and decrement stock.
- Print the total revenue.
"""


from collections import Counter


def solve() -> None:
    """
    Read input from stdin and print the total money earned.
    """
    input()  # number of shoes (not needed beyond consuming input)
    sizes = list(map(int, input().split()))
    n = int(input())

    inventory = Counter(sizes)
    total = 0

    for _ in range(n):
        size, price = map(int, input().split())
        if inventory[size] > 0:
            total += price
            inventory[size] -= 1

    print(total)


if __name__ == "__main__":
    solve()
