import pytest
from jar import Jar

def test_init():
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.deposit(-1)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(10)

def test_withdraw():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    jar.deposit(2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(3)