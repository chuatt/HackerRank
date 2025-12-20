from python.algorithms.n19_text_wrap import wrap


def test_text_wrap_sample():
    s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
    w = 4
    expected = "ABCD\nEFGH\nIJKL\nIMNO\nQRST\nUVWX\nYZ"
    assert wrap(s, w) == expected


def test_text_wrap_width_1():
    s = "HELLO"
    w = 1
    expected = "H\nE\nL\nL\nO"
    assert wrap(s, w) == expected


def test_text_wrap_exact_multiple():
    s = "ABCDEFGH"
    w = 2
    expected = "AB\nCD\nEF\nGH"
    assert wrap(s, w) == expected


def test_text_wrap_last_line_shorter():
    s = "ABCDE"
    w = 2
    expected = "AB\nCD\nE"
    assert wrap(s, w) == expected
