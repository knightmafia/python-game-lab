import sqlite3


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