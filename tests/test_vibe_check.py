from pythoncalculator import vibe_check

def test_vibe_check():
    assert vibe_check(7, 7) == "Codependent relationship. Unhealthy."
    assert vibe_check(2, 4) == "The vibes are immaculate, but I forgot the answer."
    assert vibe_check(1, 2) == "Terrible chemistry. They should see other operators."
