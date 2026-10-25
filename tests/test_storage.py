import sqlite3
from python_tests.storage import load_player, save_player_health, save_player
import pytest


@pytest.fixture
def database_path(tmp_path):
    path = tmp_path / "test.db"

    con = sqlite3.connect(path)
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            health INTEGER,
            potions INTEGER NOT NULL DEFAULT 2,
            credits INTEGER NOT NULL DEFAULT 20,
            ready_at REAL NOT NULL DEFAULT 0,
            armor INTEGER NOT NULL DEFAULT 5
        )
    """)

    con.close()
    return path

def test_load_player_returns_none_when_missing(database_path):
    result = load_player(database_path, 999)
    assert result is None

def test_load_player_returns_saved_player(database_path):
    con = sqlite3.connect(database_path)
    cur = con.cursor()

    cur.execute(
        "INSERT INTO players (id, name, health) VALUES (?, ?, ?)",
        (1, "Taco", 25),
    )

    con.commit()
    con.close()

    result = load_player(database_path, 1)

    assert result == (1, "Taco", 25, 2, 20, 0.0, 5)

def test_save_player_health_persists_change(database_path):
    con = sqlite3.connect(database_path)
    cur = con.cursor()

    cur.execute(
            "INSERT INTO players (id, name, health) VALUES (?, ?, ?)",
            (1, "Taco", 25),
        )

    con.commit()
    con.close()

    save_player_health(database_path, 1, 10)

    result = load_player(database_path, 1)
    assert result == (1, "Taco", 10, 2, 20, 0.0, 5)

def test_save_player_persists_game_state(database_path):
    con = sqlite3.connect(database_path)
    cur = con.cursor()

    cur.execute(
            "INSERT INTO players (id, name, health) VALUES (?, ?, ?)",
            (1, "Taco", 25),
        )

    con.commit()
    con.close()

    player = {
        "id": 1,
        "health": 35,
        "potions": 1,
        "credits": 10,
        "ready_at": 1900.0,
        "armor": 7,
    }

    save_player(database_path, player)

    result = load_player(database_path, 1)
    assert result == (1, "Taco", 35, 1, 10, 1900.0, 7)

def test_save_player_updates_only_requested_player(database_path):
    con = sqlite3.connect(database_path)
    cur = con.cursor()

    cur.execute(
            "INSERT INTO players (id, name, health) VALUES (?, ?, ?)",
            (1, "Taco", 25),
        )

    cur.execute(
            "INSERT INTO players (id, name, health) VALUES (?, ?, ?)",
            (2, "Nova", 80),
        )

    con.commit()
    con.close()

    player = {
    "id": 2,
    "health": 40,
    "potions": 3,
    "credits": 5,
    "ready_at": 900.0,
    "armor":7
    }

    save_player(database_path, player)
 
    taco = load_player(database_path, 1)
    nova = load_player(database_path, 2)
    assert taco == (1, "Taco", 25, 2, 20, 0.0, 5)
    assert nova == (2, "Nova", 40, 3, 5, 900.0, 7)