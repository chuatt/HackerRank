from io import StringIO

from python.algorithms.n25_collections_counter import solve


def test_collections_counter_sample(capsys, monkeypatch):
    input_data = (
        "10\n"
        "2 3 4 5 6 8 7 6 5 18\n"
        "6\n"
        "6 55\n"
        "6 45\n"
        "6 55\n"
        "4 40\n"
        "18 60\n"
        "10 50\n"
    )

    monkeypatch.setattr("sys.stdin", StringIO(input_data))

    solve()
    captured = capsys.readouterr().out
    assert captured == "200\n"


def test_collections_counter_no_sales(capsys, monkeypatch):
    input_data = (
        "3\n"
        "1 1 1\n"
        "2\n"
        "2 50\n"
        "3 60\n"
    )

    monkeypatch.setattr("sys.stdin", StringIO(input_data))

    solve()
    captured = capsys.readouterr().out
    assert captured == "0\n"
