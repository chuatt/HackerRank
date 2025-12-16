from python.algorithms.n16_find_a_string import count_substring


def test_sample():
    assert count_substring("ABCDCDC", "CDC") == 2


def test_overlapping():
    # "aaaa" contains "aa" at positions 0,1,2 (overlapping)
    assert count_substring("aaaa", "aa") == 3


def test_no_match():
    assert count_substring("abcdef", "gh") == 0


def test_full_match():
    assert count_substring("hello", "hello") == 1


def test_single_char_substring():
    assert count_substring("mississippi", "i") == 4
