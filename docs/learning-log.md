# Learning Log

## Saved health disappeared after restarting

- Symptom: Saving 10 health still loaded the original 25.
- Cause: The save function closed its connection without committing.
- Fix: Added con.commit() before con.close().
- Verification: The persistence test passed using a separate connection.
- My contribution: Investigated the failure and located the missing commit.
- Assistance: AI helped explain the failure and suggested checks.
- What I learned: Reading an update through a new connection verifies
  that it was committed.

## Fresh-clone database initialization

- Built: Added database initialization that creates the `players` table and
  starter player, then connected it to the game before loading saved state.
- Symptoms: A fresh clone had no tracked database or `players` table, and
  repeated initialization raised `sqlite3.IntegrityError` for player ID 1.
- Causes: Startup loaded the player before creating the schema, and the
  initializer originally used a normal `INSERT` for the fixed primary key.
- Fix: Initialize before loading and use `INSERT OR IGNORE` so an existing
  saved player is preserved.
- Verification: All 37 tests passed. A launch from a temporary directory with
  no database created `(1, "Taco", 100, 2, 20, 0.0, 5)` and reached the game
  prompt without modifying the existing database.
- My contribution: Chose the starter state, wrote the first-run and saved-state
  preservation tests, implemented initialization, and wired it into `main()`.
- Assistance: AI reviewed the startup path, explained the test boundaries and
  SQLite constraint failure, provided focused hints, and verified the result.
- What I learned: `sqlite3.connect()` creates a file but not its schema;
  initialization must run before queries, and it must be safe to repeat.
- Next practice topic: Add concise clone, setup, test, and run instructions to
  the README.
