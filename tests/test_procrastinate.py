from pythoncalculator import procrastinate

def test_procrastinate():
    assert procrastinate(5, 5) == "I'm not in the right headspace to calculate that right now. Ask me again next sprint."
    assert procrastinate() == "I'm not in the right headspace to calculate that right now. Ask me again next sprint."
