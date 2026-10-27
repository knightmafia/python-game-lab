# Python Game Lab

[![Tests](https://github.com/knightmafia/python-game-lab/actions/workflows/tests.yml/badge.svg?branch=master)](https://github.com/knightmafia/python-game-lab/actions/workflows/tests.yml)

A small command-line game built as a Python learning project. It practices
separating gameplay rules from input and output, testing behavior with pytest,
and persisting player state with SQLite.

## Features

- Healing with limited potions
- Damage reduction and vulnerability through armor values
- An enemy Armor Break debuff
- An Extra Life ability with a 30-minute cooldown
- A shop for buying potions with credits
- SQLite persistence for player state
- Automated tests on GitHub Actions

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/)
- Git

## Setup

Clone the repository and install its development dependencies:

```console
git clone https://github.com/knightmafia/python-game-lab.git
cd python-game-lab
uv sync --locked --dev
```

## Run the game

```console
uv run python-tests
```

On the first run, the game creates `practice_check.db` and adds a starter
player. Local database files are ignored by Git, so saved progress stays on
your machine.

The available commands are:

- `heal` — use one potion to restore up to 25 health
- `hit` — receive an enemy attack
- `debuff` — simulate an enemy Armor Break that reduces armor by 10
- `buy` — buy one potion for 10 credits
- `save` — save the current player state
- `quit` — exit the game

The game saves only when you enter `save`; quitting does not save
automatically.

## Armor and vulnerability

Positive armor reduces incoming damage. If armor is greater than the incoming
damage, the attack deals zero damage instead of healing the player.

Negative armor represents vulnerability and increases incoming damage. For
example, an attack worth `20` damage against `-5` armor deals `25` damage:

```text
20 - (-5) = 25
```

This negative-armor behavior is intentional and is covered by unit and
gameplay tests. The `debuff` command reduces armor by `10`, which changes the
starter armor from `5` to `-5`. Use `save` to persist the changed armor.

## Run the tests

Run the complete test suite:

```console
uv run --locked pytest -v
```

The tests cover healing, combat, armor, Extra Life, shopping, gameplay
interactions, and SQLite storage behavior.

## Project structure

```text
src/python_tests/
├── __init__.py          # Command-line game and entry point
├── rules.py             # Gameplay rules
└── storage.py           # SQLite initialization, loading, and saving

tests/                   # pytest test suite
docs/learning-log.md     # Notes from completed learning sessions
```

## Continuous integration

GitHub Actions installs the locked dependencies and runs the full pytest suite
for every push and pull request.
