from python_tests import use_potion

def test_potion_heals():
    assert use_potion(50, 3) == (75, 2)

def test_potion_does_not_exceed_100():
    assert use_potion(90, 3) == (100, 2)

def test_no_potion_leaves_state_unchanged():
    assert use_potion(50, 0) == (50, 0)

def test_full_health_leaves_state_unchanged():
    assert use_potion(100, 3) == (100, 3)

def test_potion_cannot_revive():
    assert use_potion(0, 2) == (0, 2)