from python_tests.rules import apply_armor, apply_armor_debuff


def test_armor_reduces_damage():
    assert apply_armor(20, 5) == 15

def test_armor_doesnt_heal():
    assert apply_armor(3, 5) == 0

def test_no_armor_damage():
    assert apply_armor(5, 0) == 5

def test_negative_armor_increases_damage():
    assert apply_armor(20, -5) == 25

def test_armor_debuff_can_create_vulnerability():
    assert apply_armor_debuff(5, 10) == -5