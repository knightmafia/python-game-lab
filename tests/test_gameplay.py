from python_tests import take_damage, use_potion, resolve_damage

def test_player_heals_after_damage():
    health = 80
    potions = 2

    health = take_damage(health, 30)
    health, potions = use_potion(health, potions)

    assert (health, potions) == (75,1)

def test_armor_prevents_lethal_damage():
    assert resolve_damage(
        10, 12, 100, 0, armor=5
    ) == (3, 0)

def test_armor_greater_than_damage():
    assert resolve_damage(
        10, 3, 100, 0, armor=5
    ) == (10, 0)

def test_extra_life_activates_when_armored_damage_is_lethal():
    assert resolve_damage(
        10, 15, 100, 0, armor=5
    ) == (25, 1900)