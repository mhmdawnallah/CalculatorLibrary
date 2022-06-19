import pytest

import calculator 

def test_add():
    assert 3 == calculator.add(1,2)


def test_substract():
    assert 2 == calculator.substract(3,1)

def test_multiplication():
    assert 100 == calculator.multiply(10,10)