# test_calculatrice.py

import pytest
from Main.src.calculatrice import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(2, -3) == -1

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-2, 3) == -5
    assert subtract(2, -3) == 5

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(6, -3) == -2
    with pytest.raises(ValueError):
        divide(6, 0)