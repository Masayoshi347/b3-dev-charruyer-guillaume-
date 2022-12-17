import math

def test_square():
    assert square(2) == 4
    assert square(0) == 0
    assert square(-2) == 4

def test_square_root():
    assert square_root(4) == 2
    assert square_root(0) == 0
    assert square_root(2) == math.sqrt(2)

def test_power():
    assert power(2, 2) == 4
    assert power(2, 0) == 1
    assert power(0, 2) == 0
    assert power(2, 3) == 8
