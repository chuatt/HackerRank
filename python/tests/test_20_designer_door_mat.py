from python.algorithms.n20_designer_door_mat import print_door_mat


def test_designer_door_mat_7x21(capsys):
    """
    Test sample-style design for N=7, M=21.
    """
    print_door_mat(7, 21)
    captured = capsys.readouterr().out

    expected = (
        "---------.|.---------\n"
        "------.|..|..|.------\n"
        "---.|..|..|..|..|.---\n"
        "-------WELCOME-------\n"
        "---.|..|..|..|..|.---\n"
        "------.|..|..|.------\n"
        "---------.|.---------\n"
    )

    assert captured == expected


def test_designer_door_mat_9x27(capsys):
    """
    Test the given sample input/output in the prompt: 9 27.
    """
    print_door_mat(9, 27)
    captured = capsys.readouterr().out

    expected = (
        "------------.|.------------\n"
        "---------.|..|..|.---------\n"
        "------.|..|..|..|..|.------\n"
        "---.|..|..|..|..|..|..|.---\n"
        "----------WELCOME----------\n"
        "---.|..|..|..|..|..|..|.---\n"
        "------.|..|..|..|..|.------\n"
        "---------.|..|..|.---------\n"
        "------------.|.------------\n"
    )

    assert captured == expected


def test_designer_door_mat_min_size_1x3(capsys):
    """
    Edge case: smallest odd N=1, M must be 3.
    """
    print_door_mat(1, 3)
    captured = capsys.readouterr().out

    expected = "WELCOME\n"
    assert captured == expected
