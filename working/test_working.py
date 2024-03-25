import pytest
from working import convert


def test_convert():
    assert convert("9:30 AM to 7:50 PM") == "09:30 to 19:50"
    assert convert("9 AM to 7 PM") == "09:00 to 19:00"
    with pytest.raises(ValueError):
        convert("dsfsdfdsfs")
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")
    with pytest.raises(ValueError):
         convert("9:60 AM to 9:60 PM")