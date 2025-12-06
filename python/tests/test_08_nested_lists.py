from python.algorithms.n08_nested_lists import second_lowest_students


def test_sample_case():
    # Sample from the HackerRank description
    records = [
        ["Harry", 37.21],
        ["Berry", 37.21],
        ["Tina", 37.2],
        ["Akriti", 41.0],
        ["Harsh", 39.0],
    ]
    # Unique grades: [37.2, 37.21, 39.0, 41.0]
    # Second lowest = 37.21 → Harry, Berry → alphabetical: Berry, Harry
    assert second_lowest_students(records) == ["Berry", "Harry"]


def test_two_students_simple():
    records = [
        ["Alice", 10.0],
        ["Bob", 20.0],
    ]
    # Lowest = 10, second lowest = 20
    assert second_lowest_students(records) == ["Bob"]


def test_multiple_with_second_lowest():
    records = [
        ["Zara", 50.0],
        ["Liam", 40.0],
        ["Noah", 40.0],
        ["Mia", 60.0],
    ]
    # Unique grades: [40, 50, 60] → second lowest = 50
    assert second_lowest_students(records) == ["Zara"]


def test_alphabetical_order():
    records = [
        ["delta", 70.0],
        ["bravo", 50.0],
        ["charlie", 50.0],
        ["alpha", 30.0],
    ]
    # Second lowest = 50 → bravo, charlie → alphabetical
    assert second_lowest_students(records) == ["bravo", "charlie"]


def test_float_precision_like_values():
    records = [
        ["A", 10.0],
        ["B", 10.0001],
        ["C", 10.0001],
        ["D", 11.0],
    ]
    # Unique grades: [10.0, 10.0001, 11.0] → second lowest = 10.0001
    assert second_lowest_students(records) == ["B", "C"]
