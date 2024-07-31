import pytest

from twttr import shorten

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_lowercase():
    assert shorten ("hello") == "hll"

def test_numbers():
    assert shorten("1") == "1"
    assert shorten("10") == "10"

def test_punctuation_marks():
    assert shorten("_hello_") == "_hll_"
    assert shorten("_h_e_l_l_o_") == "_h__l_l__"
    assert shorten("hello?") == "hll?"

def test_spaces():
    assert shorten("   hello") == "   hll"
    assert shorten("hello   ") == "hll   "
    assert shorten("h e l l o") == "h  l l "