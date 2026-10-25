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