from python.algorithms.n18_text_alignment import print_hackerrank_logo


def test_text_alignment_thickness_3(capsys):
    print_hackerrank_logo(3)
    captured = capsys.readouterr().out

    expected = (
        "  H  \n"
        " HHH \n"
        "HHHHH\n"
        " HHH         HHH        \n"
        " HHH         HHH        \n"
        " HHH         HHH        \n"
        " HHH         HHH        \n"
        " HHHHHHHHHHHHHHH  \n"
        " HHHHHHHHHHHHHHH  \n"
        " HHH         HHH        \n"
        " HHH         HHH        \n"
        " HHH         HHH        \n"
        " HHH         HHH        \n"
        "            HHHHH \n"
        "             HHH  \n"
        "              H   \n"
    )

    assert captured == expected


def test_text_alignment_thickness_1(capsys):
    print_hackerrank_logo(1)
    captured = capsys.readouterr().out

    expected = (
        "H\n"
        "H   H   \n"
        "H   H   \n"
        "HHHHH \n"
        "H   H   \n"
        "H   H   \n"
        "    H \n"
    )

    assert captured == expected
