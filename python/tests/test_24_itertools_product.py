from python.algorithms.n24_itertools_product import solve


def test_itertools_product_basic(capsys, monkeypatch):
    input_data = iter(["1 2", "3 4"])
    monkeypatch.setattr("builtins.input", lambda: next(input_data))

    solve()
    captured = capsys.readouterr().out
    assert captured == "(1, 3) (1, 4) (2, 3) (2, 4)\n"


def test_itertools_product_single_element(capsys, monkeypatch):
    input_data = iter(["5", "10"])
    monkeypatch.setattr("builtins.input", lambda: next(input_data))

    solve()
    captured = capsys.readouterr().out
    assert captured == "(5, 10)\n"
