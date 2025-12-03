from python.algorithms.n01_python_if_else import weird_or_not


def test_odd_numbers_are_weird():
    assert weird_or_not(3) == "Weird"
    assert weird_or_not(1) == "Weird"


def test_even_2_to_5_not_weird():
    assert weird_or_not(2) == "Not Weird"
    assert weird_or_not(4) == "Not Weird"


def test_even_6_to_20_weird():
    assert weird_or_not(6) == "Weird"
    assert weird_or_not(20) == "Weird"


def test_even_above_20_not_weird():
    assert weird_or_not(22) == "Not Weird"
    assert weird_or_not(100) == "Not Weird"
