from python.algorithms.n03_python_division import division_results


def test_division_basic():
    int_res, float_res = division_results(3, 5)
    assert int_res == 0
    assert float_res == 0.6


def test_division_sample():
    int_res, float_res = division_results(4, 3)
    assert int_res == 1
    assert float_res == 4 / 3
