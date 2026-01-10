from io import StringIO

from python.algorithms.n26_itertools_permutations import solve


def test_itertools_permutations_sample(capsys, monkeypatch):
    input_data = "HACK 2\n"
    expected_output = (
        "AC\n"
        "AH\n"
        "AK\n"
        "CA\n"
        "CH\n"
        "CK\n"
        "HA\n"
        "HC\n"
        "HK\n"
        "KA\n"
        "KC\n"
        "KH\n"
    )

    monkeypatch.setattr("sys.stdin", StringIO(input_data))

    solve()
    captured = capsys.readouterr().out
    assert captured == expected_output


def test_itertools_permutations_full_length(capsys, monkeypatch):
    input_data = "ABC 3\n"
    expected_output = (
        "ABC\n"
        "ACB\n"
        "BAC\n"
        "BCA\n"
        "CAB\n"
        "CBA\n"
    )

    monkeypatch.setattr("sys.stdin", StringIO(input_data))

    solve()
    captured = capsys.readouterr().out
    assert captured == expected_output
