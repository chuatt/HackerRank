from python.algorithms.n14_whats_your_name import print_full_name


def test_print_full_name(capsys):
    print_full_name("Ross", "Taylor")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "Hello Ross Taylor! You just delved into python.\n"
    )
