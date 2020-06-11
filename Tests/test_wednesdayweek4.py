import pytest
from Code.wednesdayweek4 import mergewords

def test_mergewords():
    assert mergewords("String", "Fridge") == "SFtrriidngge"