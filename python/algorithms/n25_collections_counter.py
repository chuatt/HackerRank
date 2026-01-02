from collections import Counter

def solve() -> None:
    x = int(input())
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
