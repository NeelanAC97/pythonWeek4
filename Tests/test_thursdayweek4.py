import pytest
from Code.thursdayweek4 import prime_no_checker

def test_prime_no_checker1():
    assert prime_no_checker(1) == False

def test_prime_no_checker2():
    assert prime_no_checker(2) == True

def test_prime_no_checker3():
    assert prime_no_checker(3) == True

def test_prime_no_checker4():
    assert prime_no_checker(8) == False

def test_prime_no_checker3():
    assert prime_no_checker(97) == True

def test_prime_no_checker3():
    assert prime_no_checker(64) == False




