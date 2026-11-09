from pythoncalculator import divide_unevenly

def test_divide_unevenly():
    assert divide_unevenly(100, 2) == "Here is your share: 21.0. I kept the rest."
    assert divide_unevenly(10, 0) == "You broke the universe. Happy now?"
