import pytest

from calculator import *

def test_add():
    assert 3 == add(1,2)


def test_substract():
    assert 2 == substract(3,1)

