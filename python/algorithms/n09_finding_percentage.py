"""
Problem: Finding the Percentage
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/finding-the-percentage/problem

Summary:
You are given student records consisting of a name and three marks. After
 reading n such records, you must compute and print the average of the marks
 for a requested student, formatted to 2 decimal places.

Example:
Records:
alpha → [20, 30, 40]
beta  → [30, 50, 70]
Query: "beta"
Average = (30 + 50 + 70) / 3 = 50.00

Approach:
1. Read n records into a dictionary mapping names → list of float scores.
2. Compute the mean of the list for the queried student.
3. Format the result to 2 decimal places.

Constraints:
2 ≤ n ≤ 10
0 ≤ marks[i] ≤ 100
Each student has exactly 3 marks.
"""


def student_average(student_marks: dict[str, list[float]], name: str) -> float:
    """Return the average score for the given student."""
    scores = student_marks[name]
    return sum(scores) / len(scores)


if __name__ == "__main__":
    count = int(input().strip())
    students: dict[str, list[float]] = {}

    for _ in range(count):
        parts = input().split()
        name, scores = parts[0], list(map(float, parts[1:]))
        students[name] = scores

    query_name = input().strip()
    avg = student_average(students, query_name)

    # Print formatted to 2 decimal places
    print(f"{avg:.2f}")
