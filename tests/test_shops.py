from python_tests.rules import buy_potion

def test_has_more_than_enough_credits():
    assert buy_potion(25, 2) == (15, 3)

def test_has_exactly_enough_credits():
    assert buy_potion(10, 2) == (0, 3)

def test_does_not_have_enough_credits():
    assert buy_potion(2, 2) == (2, 2)