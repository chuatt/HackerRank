"""
Problem: Python Lists
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/python-lists/problem

Summary:
You are given a list of commands that manipulate a Python list. Each command
corresponds to a list operation: insert, print, remove, append, sort, pop,
or reverse. Your task is to process all the commands and return the results
of every `print` operation.

Example:
Commands:
insert 0 5     → arr = [5]
insert 1 10    → arr = [5, 10]
insert 0 6     → arr = [6, 5, 10]
print          → output: [6, 5, 10]
remove 6       → arr = [5, 10]
append 9       → arr = [5, 10, 9]
append 1       → arr = [5, 10, 9, 1]
sort           → arr = [1, 5, 9, 10]
print          → output: [1, 5, 9, 10]
pop            → arr = [1, 5, 9]
reverse        → arr = [9, 5, 1]
print          → output: [9, 5, 1]

Approach:
1. Parse each command and split it into tokens.
2. Perform the corresponding list operation.
3. Whenever the command is `print`, append a copy of the list to outputs.
4. Return all printed snapshots for testing purposes.

Constraints:
• The list initially starts empty.
• All inserted/appended values are integers.
• Valid commands include: insert, print, append, remove, pop, sort, reverse.
"""


def process_commands(commands: list[str]) -> list[list[int]]:
    """Execute list commands and return outputs for print."""
    arr: list[int] = []
    outputs: list[list[int]] = []

    for command in commands:
        parts = command.strip().split()
        cmd = parts[0]

        if cmd == "insert":
            i, e = int(parts[1]), int(parts[2])
            arr.insert(i, e)

        elif cmd == "print":
            outputs.append(arr.copy())

        elif cmd == "append":
            e = int(parts[1])
            arr.append(e)

        elif cmd == "remove":
            e = int(parts[1])
            arr.remove(e)

        elif cmd == "pop":
            arr.pop()

        elif cmd == "sort":
            arr.sort()

        elif cmd == "reverse":
            arr.reverse()

    return outputs


if __name__ == "__main__":
    n = int(input().strip())
    cmds = [input().strip() for _ in range(n)]

    result = process_commands(cmds)
    for state in result:
        print(state)
