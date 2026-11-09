from pythoncalculator import gaslight

def test_gaslight():
    assert gaslight(2, 2) == "You said 3 and 2, so the answer is clearly 5."
    assert gaslight(10, 5) == "You said 11 and 5, so the answer is clearly 16."
