"""
Use Ctrl + I to generate code

Problem: Nested Lists
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/nested-list/problem

Summary:
Given N students with their names and grades, print the name(s) of the student(s)
having the second lowest grade.

If more than one student has the second lowest grade, print all such names in
alphabetical order.

Example:
records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
Unique sorted grades → [20.0, 50.0]
Second lowest → 50.0
Students with grade 50.0 → ["alpha", "beta"]

Approach:
1. Parse input into a list of [name, grade].
2. Extract all unique grades and sort them.
3. Find the second lowest grade.
4. Collect names matching that grade.
5. Sort names alphabetically and return the list.

Constraints:
2 ≤ N ≤ 5
There will always be at least one student with the second lowest grade.

This file follows the clean consistent style used across the repository.
"""


def second_lowest_students(records: list[list]) -> list[str]:
    """Return a list of names with the second lowest grade."""
    grades = sorted({grade for _, grade in records})
    second_lowest = grades[1]

    return sorted(name for name, grade in records if grade == second_lowest)


if __name__ == "__main__":
    n = int(input().strip())

    students = []
    for _ in range(n):
        name = input().strip()
        grade = float(input().strip())
        students.append([name, grade])

    for student in second_lowest_students(students):
        print(student)
