import pytest
from bank import value

def test_greeting():
    assert value("hello") == 0
    assert value("hello, world") == 0
    assert value("honda") == 20
    assert value("honda, wonda") == 20
    assert value("anaconda") == 100
    assert value("anaconda snake") == 100

def test_casing():
    assert value("HELLO") == 0
    assert value("HONDA") == 20
    assert value("ANACONDA") == 100
    assert value("HeLLo") == 0

def test_punctuation():
    assert value("Hello?") == 0
    assert value("Honda?") == 20
    assert value("Anaconda?") == 100
    assert value("H_ell_o") == 20
    assert value("H_ond_a") == 20
    assert value("A_naco_nd_a") == 100

def test_numbers():
    assert value("0") == 100
    assert value("1") == 100
    assert value("10") == 100