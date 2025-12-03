from python.algorithms.n05_write_a_function_leap_year import is_leap


def test_divisible_by_400():
    assert is_leap(2000) is True
    assert is_leap(2400) is True


def test_divisible_by_100_not_400():
    assert is_leap(1900) is False
    assert is_leap(2100) is False


def test_divisible_by_4_not_100():
    assert is_leap(1996) is True
    assert is_leap(2012) is True


def test_not_divisible_by_4():
    assert is_leap(1990) is False
    assert is_leap(2019) is False
