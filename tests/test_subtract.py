from pythoncalculator import subtract
from pythoncalculator import subtract2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 4) == 6
    assert subtract(0, 0) == 0

def test_subtract2():
    """Like the other test_subtract function, but written by the person assigned to it"""
    assert subtract2(1, 1) == 0
    assert subtract2(2, 1) == 1
    assert subtract2(3, 1) == 2
    assert subtract2(4, 2) == 2
    assert subtract2(5, 1) == 4
    assert subtract2(6, 3) == 3
    assert subtract2(7, 2) == 5
    assert subtract2(8, 5) == 3
    assert subtract2(9, 3) == 6
    assert subtract2(10, 5) == 5
    assert subtract2(11, 4) == 7
    assert subtract2(12, 6) == 6
    assert subtract2(15, 7) == 8
    assert subtract2(20, 8) == 12
    assert subtract2(25, 10) == 15
    assert subtract2(30, 12) == 18
    assert subtract2(45, 15) == 30
    assert subtract2(50, 25) == 25
    assert subtract2(75, 25) == 50
    assert subtract2(100, 33) == 67
    assert subtract2(100, 50) == 50
    assert subtract2(150, 50) == 100
    assert subtract2(200, 75) == 125
    assert subtract2(500, 200) == 300
    assert subtract2(1000, 400) == 600
    assert subtract2(1, 0) == 1
    assert subtract2(5, 0) == 5
    assert subtract2(42, 0) == 42
    assert subtract2(100, 0) == 100
    assert subtract2(3, 3) == 0
    assert subtract2(10, 10) == 0
    assert subtract2(99, 99) == 0
    assert subtract2(0, 5) == -5
    assert subtract2(0, 10) == -10
    assert subtract2(3, 8) == -5
    assert subtract2(5, 10) == -5
    assert subtract2(10, 20) == -10
    assert subtract2(15, 45) == -30
    assert subtract2(50, 100) == -50
    assert subtract2(-5, -3) == -2
    assert subtract2(-10, -4) == -6
    assert subtract2(-5, -5) == 0
    assert subtract2(-1, -1) == 0
    assert subtract2(-10, -20) == 10
    assert subtract2(-5, 3) == -8
    assert subtract2(-10, 5) == -15
    assert subtract2(-1, 9) == -10
    assert subtract2(-50, 25) == -75
    assert subtract2(5, -3) == 8
    assert subtract2(10, -4) == 14
    assert subtract2(0, -5) == 5
    assert subtract2(15, -10) == 25
    assert subtract2(100, -50) == 150
    assert subtract2(1.5, 0.5) == 1.0
    assert subtract2(5.5, 2.25) == 3.25
    assert subtract2(10.0, 4.5) == 5.5
    assert subtract2(0.5, 0.25) == 0.25
    assert subtract2(3.14, 1.14) == 2.0
    assert subtract2(1000000, 500000) == 500000
    assert subtract2(1000000000, 1) == 999999999
    assert subtract2(999999, 999998) == 1