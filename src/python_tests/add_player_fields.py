import sqlite3

con = sqlite3.connect("practice_check.db")

cur = con.cursor()

add_potions_query = """
ALTER TABLE players
ADD COLUMN potions INTEGER NOT NULL DEFAULT 2;
"""

# cur.execute(add_potions_query)

add_credits_query = """
ALTER TABLE players
ADD COLUMN credits INTEGER NOT NULL DEFAULT 20;
"""

# cur.execute(add_credits_query)

add_ready_at_query = """
ALTER TABLE players
ADD COLUMN ready_at REAL NOT NULL DEFAULT 0;
"""

# cur.execute(add_ready_at_query)

add_armor_query = """
ALTER TABLE players
ADD COLUMN armor INTEGER NOT NULL DEFAULT 5;
"""

cur.execute(add_armor_query)

cur.execute(
    "SELECT * FROM players"
)

print(cur.fetchall())

con.close()