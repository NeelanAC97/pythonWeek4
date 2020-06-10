import pytest 
from Code.tuesdayweek4 import func

def test_func():
    assert func("without,hello,bag,world") == ['bag', 'hello', 'without', 'world']