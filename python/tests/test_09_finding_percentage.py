from python.algorithms.n09_finding_percentage import student_average


def test_sample_case():
    # Example from the HackerRank problem statement
    student_marks = {
        "Krishna": [67.0, 68.0, 69.0],
        "Arjun": [70.0, 98.0, 63.0],
        "Malika": [52.0, 56.0, 60.0],
    }
    result = student_average(student_marks, "Malika")
    assert round(result, 2) == 56.00


def test_exact_two_decimal_format():
    student_marks = {"alpha": [30.0, 50.0, 70.0]}
    result = student_average(student_marks, "alpha")
    assert round(result, 2) == 50.00


def test_all_marks_same():
    student_marks = {"beta": [40.0, 40.0, 40.0]}
    result = student_average(student_marks, "beta")
    assert result == 40.0


def test_decimal_inputs():
    student_marks = {"gamma": [10.5, 20.5, 30.5]}
    result = student_average(student_marks, "gamma")
    assert round(result, 2) == 20.50


def test_edge_min_values():
    student_marks = {"min": [0.0, 0.0, 0.0]}
    result = student_average(student_marks, "min")
    assert result == 0.0


def test_edge_max_values():
    student_marks = {"max": [100.0, 100.0, 100.0]}
    result = student_average(student_marks, "max")
    assert result == 100.0
