from python.algorithms.n18_text_alignment import print_hackerrank_logo


def test_text_alignment_thickness_3(capsys):
    """
    Test HackerRank logo output for thickness = 3.
    """
    print_hackerrank_logo(3)
    captured = capsys.readouterr().out

    expected = (
        "  H  \n"
        " HHH \n"
        "HHHHH\n"
        "HHH   HHH\n"
        "HHH   HHH\n"
        "HHHHHHHHH\n"
        "HHH   HHH\n"
        "HHH   HHH\n"
        "  HHHHH  \n"
        "    HHH  \n"
        "      H  \n"
    )

    assert captured == expected


def test_text_alignment_thickness_1(capsys):
    """
    Edge case: smallest valid thickness.
    """
    print_hackerrank_logo(1)
    captured = capsys.readouterr().out

    expected = (
        "H\n"
        "H H\n"
        "HHH\n"
        "H H\n"
        "H\n"
    )

    assert captured == expected
