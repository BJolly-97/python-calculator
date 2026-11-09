from pythoncalculator import subtract
from pythoncalculator import subtract2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(0, 0) == 0

def test_subtract2():
    """Like the other test_subtract function, but written by the person assigned to it"""
    assert subtract2(5, 3) == 2
    assert subtract2(10, 4) == 6
    assert subtract2(0, 0) == 0