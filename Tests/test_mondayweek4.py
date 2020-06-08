import pytest
from Code.mondayweek4 import func

def test_func():
    assert func(2) == 2468

def test_func2():
    assert func(-2) == "Bad input"

def test_func3():
    assert func(9) == 11106

def test_func4():
    assert func(5) == 6170