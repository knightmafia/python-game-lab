from python_tests import main
from python_tests.storage import load_player


def test_main_creates_database_on_first_run(tmp_path, monkeypatch, capsys):
    # Arrange
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr("builtins.input", lambda prompt: "quit")
    # Act
    main()
    captured = capsys.readouterr()
    # Assert
    database_path = tmp_path / "practice_check.db"
    assert database_path.exists()

    starter_player = load_player(database_path, 1)

    assert starter_player == (1, "Taco", 100, 2, 20, 0.0, 5)
    assert "Goodbye!" in captured.out


def test_main_saves_player_after_hit(tmp_path, monkeypatch, capsys):
    # Arrange
    monkeypatch.chdir(tmp_path)
    actions = iter(["hit", "save", "quit"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(actions))
    # Act
    main()
    captured = capsys.readouterr()
    # Assert
    database_path = tmp_path / "practice_check.db"
    assert database_path.exists()

    saved_player = load_player(database_path, 1)

    assert saved_player == (1, "Taco", 75, 2, 20, 0.0, 5)
    assert "Player Saved!" in captured.out
    assert "Goodbye!" in captured.out
