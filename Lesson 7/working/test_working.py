import pytest
from working import convert

def test_value_error():
    with pytest.raises(ValueError):
        convert("12 AM - 12 PM")
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:45 PM")
    with pytest.raises(ValueError):
        convert("8:00 AM to 4:60 PM")

def test_period():
    with pytest.raises(ValueError):
        convert("11AM to 5PM")
    with pytest.raises(ValueError):
        convert("11  AM to 5  PM")

def test_hour():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("8:30 PM to 9:15 AM") == "20:30 to 09:15"