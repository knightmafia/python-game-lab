from python_tests.rules import apply_armor


def test_armor_reduces_damage():
    assert apply_armor(20, 5) == 15

def test_armor_doesnt_heal():
    assert apply_armor(3, 5) == 0

def test_no_armor_damage():
    assert apply_armor(5, 0) == 5