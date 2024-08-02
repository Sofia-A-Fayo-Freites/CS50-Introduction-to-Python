import pytest
from um import count

def test_case():
    assert count("UM") == 1
    assert count("um") == 1
    assert count("Um") == 1
    assert count("uM") == 1

def test_length():
    assert count("ummm") == 0
    assert count("u ") == 0
    assert count("um") == 1

def test_counting():
    assert count("um, um, um") == 3
    assert count("um") == 1
    assert count("yummy") == 0