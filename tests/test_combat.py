from python_tests import take_damage
import pytest

def test_damage_reduces_health():
    assert take_damage(80, 20) == 60

def test_damage_exceeds_health():
    assert take_damage(15, 25) == 0

def test_zero_damage():
    assert take_damage(15, 0) == 15

def test_negative_damage_is_rejected():
    with pytest.raises(ValueError):
        take_damage(50, -10)