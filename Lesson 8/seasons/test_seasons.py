import pytest
from seasons import calculate_minutes

def test_sys_exit():
    with pytest.raises(SystemExit):
        calculate_minutes("cat")
    with pytest.raises(SystemExit):
        calculate_minutes("1999/01/16")

def test_minutes():
    assert calculate_minutes("1992-02-07") == "Seventeen million, eighty-nine thousand, nine hundred twenty"
    assert calculate_minutes("2024-08-05") == "Zero"
    assert calculate_minutes("2023-08-05") == "Five hundred twenty-seven thousand forty"
