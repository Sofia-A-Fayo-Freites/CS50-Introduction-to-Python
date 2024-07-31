import pytest
from fuel import convert, gauge

def test_ValueError_X_larger_than_Y():
    with pytest.raises(ValueError):
        convert("2/1")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert():
    assert convert("1/4") == 25

def test_E():
    assert gauge(1) == "E"

def test_F():
    assert gauge(99) == "F"

def test_percentage():
    assert gauge(25) == "25%"