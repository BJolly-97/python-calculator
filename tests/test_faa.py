from pythoncalculator import faa

def test_faa():
    assert faa(5, 3) == None
    assert faa(10, 4) == None
    assert faa(0, 0) == None