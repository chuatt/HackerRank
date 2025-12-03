from python.algorithms.n04_python_loops import squares_upto


def test_small_n():
    assert squares_upto(3) == [0, 1, 4]


def test_sample_n():
    assert squares_upto(5) == [0, 1, 4, 9, 16]
