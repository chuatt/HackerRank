from python.algorithms.n23_capitalize import solve


def test_capitalize_sample(capsys):
    solve("chris alan")
    captured = capsys.readouterr().out
    assert captured == "Chris Alan\n"


def test_capitalize_multiple_spaces_preserved(capsys):
    solve("  chris   alan  ")
    captured = capsys.readouterr().out
    assert captured == "  Chris   Alan  \n"


def test_capitalize_alphanumeric_words(capsys):
    solve("12abc 3g test1")
    captured = capsys.readouterr().out
    assert captured == "12abc 3g Test1\n"
