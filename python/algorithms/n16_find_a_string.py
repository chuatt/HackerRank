"""
Problem: Find a string
Platform: HackerRank
Link:
https://www.hackerrank.com/challenges/find-a-string/problem

Summary:
Given a string and a substring, count how many times the substring occurs in the
string. Overlapping occurrences ARE counted.

Example:
String:    ABCDCDC
Substring: CDC
Count = 2  (positions 2 and 4)

Approach:
Slide a window of length len(sub_string) across the string and compare slices.
Increment the counter whenever the slice matches.

Constraints:
1 <= len(string) <= 200
"""


def count_substring(string: str, sub_string: str) -> int:
    """Return the number of (overlapping) occurrences of sub_string in string."""
    count = 0
    sub_len = len(sub_string)

    for i in range(len(string) - sub_len + 1):
        if string[i : i + sub_len] == sub_string:
            count += 1

    return count


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()
    print(count_substring(string, sub_string))
