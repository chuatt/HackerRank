from python.algorithms.n07_runner_up_score import runner_up_score


def test_sample_case():
    # From the HackerRank example: 2 3 6 6 5 → runner-up is 5
    values = [2, 3, 6, 6, 5]
    assert runner_up_score(values) == 5


def test_strictly_increasing():
    values = [1, 2, 3, 4]
    assert runner_up_score(values) == 3


def test_strictly_decreasing():
    values = [9, 7, 5, 3]
    assert runner_up_score(values) == 7


def test_with_duplicates_and_negatives():
    values = [-10, -10, -5, -3, -3, -1]
    # Unique sorted: [-10, -5, -3, -1] → runner-up is -3
    assert runner_up_score(values) == -3


def test_minimum_valid_length():
    # Smallest n where two unique values exist
    values = [1, 2]
    assert runner_up_score(values) == 1


def test_runner_up_with_many_duplicates_of_max():
    values = [4, 4, 4, 2, 2, 3, 4]
    # Unique sorted: [2, 3, 4] → runner-up is 3
    assert runner_up_score(values) == 3
