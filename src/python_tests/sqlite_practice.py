import sqlite3
from python_tests.storage import load_player

print(load_player("practice_check.db", 1))
print(load_player("practice_check.db", 999))

# con = sqlite3.connect("practice_check.db")

# cur = con.cursor()

# create_query = """
# CREATE TABLE IF NOT EXISTS players(
# id INTEGER PRIMARY KEY, 
# name TEXT, 
# health INTEGER)
# """

# cur.execute(create_query)

# insert_query = """
# INSERT INTO players (name, health)
# VALUES (?,?) 
# """

# # cur.execute(insert_query, ("Taco", 50))

# update_query = """
# UPDATE players
# SET health = ?
# WHERE id = ?
# """

# cur.execute(update_query, (25, 1))
# con.commit()
# cur.execute(
#     "SELECT id, name, health FROM players WHERE id = ?",
#     (1,),
# )
# print(cur.fetchall())

# con.close()