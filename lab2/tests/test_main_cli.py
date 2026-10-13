
from lab.main import main


def test_menu_exit(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "0")
    main()
    captured = capsys.readouterr()
    assert "Меню" in captured.out
    assert "завершена" in captured.out


def test_menu_invalid_choice(monkeypatch, capsys):

    inputs = iter(["x", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Неверный пункт" in captured.out


def test_menu_load(monkeypatch, capsys):
    inputs = iter(["1", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Загружено" in captured.out


def test_menu_show(monkeypatch, capsys):
    inputs = iter(["1", "", "", "3", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    main()
    captured = capsys.readouterr()
    assert "Иванов" in captured.out or "id" in captured.out