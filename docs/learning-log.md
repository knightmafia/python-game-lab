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

## CLI integration and rule validation

- Built: Expanded the README and package description, added entry-point tests
  for first run, saving, quitting without saving, and normalized commands.
- Bugs: Mixed-case or padded commands were rejected, and negative damage with
  armor was changed to zero instead of raising `ValueError`.
- Causes: Input was compared without normalization, and armor transformed the
  damage before the existing validation could inspect its original value.
- Fixes: Normalize input with `strip().lower()` and validate raw damage before
  applying armor.
- Design decision: Negative armor intentionally represents vulnerability; unit
  and gameplay tests now document that it increases incoming damage.
- Git issue: Pushes failed because a GitHub CLI credential override bypassed
  Git Credential Manager. Removing the override restored normal pushes.
- Verification: The complete suite passed with 44 tests, focused tests covered
  each behavior, and all completed commits were pushed to `master`.
- My contribution: Wrote the implementation and tests, chose the vulnerability
  behavior, interpreted failures, and corrected formatting issues.
- Assistance: AI drafted the README, provided incremental testing hints and
  reviews, verified results, managed commits, and diagnosed Git authentication.
- What I learned: `tmp_path`, `monkeypatch`, and `capsys` can safely test an
  interactive entry point; persisted state changes only on save; validation
  must occur before calculations can hide invalid input.
- Next practice topic: Document vulnerability in the README and decide how
  gameplay can apply negative armor to a player.
