from python_tests import can_trigger_extra_life, try_extra_life, resolve_damage

def test_extra_life_unavailable_during_cooldown():
    assert can_trigger_extra_life(0, 500, 600) == False

def test_extra_life_ready_but_life_not_zero():
    assert can_trigger_extra_life(5, 500, 500) == False

def test_extra_life_ready_no_cooldown():
    assert can_trigger_extra_life(0, 500,500) == True

def test_extra_life_ready_after_cooldown():
    assert can_trigger_extra_life(0, 700, 600) == True

def test_extra_life_revives_and_starts_cooldown():
    assert try_extra_life(0, 100, 0) == (25, 1900)

def test_extra_life_does_not_revive_during_cooldown():
    assert try_extra_life(0, 100, 500) == (0, 500)

def test_extra_life_does_not_revive_while_alive():
    assert try_extra_life(1, 100, 0) == (1, 0)

def test_lethal_damage_automatically_triggers_extra_life():
    assert resolve_damage(20, 30, 100, 0) == (25, 1900)

def test_lethal_damage_during_cooldown():
    assert resolve_damage(20, 30, 100, 1000) == (0, 1000)

def test_nonletal_damage_with_extra_life_avaiable():
    assert resolve_damage(20, 5, 100, 0) == (15, 0)

def test_extra_life_cannot_rescue_twice_during_cooldown():
    health = 20
    ready_at = 0

    health, ready_at = resolve_damage(
        health, 30, 100, ready_at
    )
    assert (health, ready_at) == (25, 1900)

    health, ready_at = resolve_damage(
        health, 30, 200, ready_at
    )
    assert (health, ready_at) == (0, 1900)