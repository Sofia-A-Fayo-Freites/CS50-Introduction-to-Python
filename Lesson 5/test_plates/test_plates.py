import pytest
from plates import is_valid

def test_casing():
    assert is_valid("AA12") == True
    assert is_valid("aa12") == True

def test_numbers():
    assert is_valid("12345") == False

def test_length():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AA1") == True
    assert is_valid("AA12") == True
    assert is_valid("AA123") == True
    assert is_valid("AA1234") == True
    assert is_valid("AA12345") == False

def test_zero_placement():
    assert is_valid("AA01") == False

def test_alnum():
    assert is_valid("12AA") == False
    assert is_valid("01AA") == False
    assert is_valid("AAA12A") == False

def test_punctuation():
    assert is_valid("AA12*") == False
    assert is_valid("*AA12") == False
    assert is_valid("*AA12*") == False

def test_spaces():
    assert is_valid(" AA12") == False
    assert is_valid("AA12 ") == False
    assert is_valid(" AA12 ") == False
