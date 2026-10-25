import sqlite3


def initialize_database(database_path):
    database_query = """
        CREATE TABLE IF NOT EXISTS players (
        id INTEGER PRIMARY KEY,
        name TEXT,
        health INTEGER,
        potions INTEGER NOT NULL DEFAULT 2,
        credits INTEGER NOT NULL DEFAULT 20,
        ready_at REAL NOT NULL DEFAULT 0,
        armor INTEGER NOT NULL DEFAULT 5
        )
    """
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    cur.execute(database_query)
    cur.execute(
        "INSERT OR IGNORE INTO players (id, name, health) VALUES (?, ?, ?)",
        (1, "Taco", 100),
    )
    con.commit()
    con.close()


def load_player(database_path, player_id):
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    query = """
    SELECT id, name, health, potions, credits, ready_at, armor
    FROM players
    WHERE id = ?
    """
    cur.execute(query, (player_id,))

    row = cur.fetchone()
    con.close()

    return row

def save_player_health(database_path, player_id, health):
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    query = """
    UPDATE players
    SET health = ?
    WHERE id = ?
    """
    cur.execute(query, (health, player_id,))

    con.commit()
    row = cur.fetchone()
    con.close()

    return row

def save_player(database_path, player):
    con = sqlite3.connect(database_path)
    cur = con.cursor()
    query = """
    UPDATE players
    SET health = ?, potions = ?, credits = ?, ready_at = ?, armor = ?
    WHERE id = ?
    """
    cur.execute(query, (
        player["health"], 
        player["potions"], 
        player["credits"], 
        player["ready_at"],
        player["armor"],
        player["id"],
        ))

    con.commit()
    con.close()