import pytest
from numb3rs import validate

def test_ip_number():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("10.12.536.895") == False
    assert validate("256.256.256.256") == False
    assert validate("1000.1000.1000.1000") == False

def test_ip_syntax():
    assert validate("0.0.0") == False
    assert validate(".3.12.15") == False
    assert validate("0.0.0.0.") == False
    assert validate("python") == False