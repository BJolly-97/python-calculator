from pythoncalculator import subtract

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(0, 0) == 0