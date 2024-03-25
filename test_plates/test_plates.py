from plates import is_valid


def test_is_valid_1():
    assert is_valid("AA232A") == False

def test_is_valid_2():
    assert is_valid("SDFJDSJFDSJFDS") == False

def test_is_valid_3():
    assert is_valid("12323A") == False

def test_is_valid_4():
    assert is_valid("AA0323A") == False

def test_is_valid_5():
    assert is_valid("AAA003") == False

def test_is_valid_6():
    assert is_valid("124545") == False

def test_is_valid_7():
    assert is_valid("") == False

def test_is_valid_8():
    assert is_valid("AA") == True

def test_is_valid_9():
    assert is_valid("A2") == False
def test_is_valid_10():
    assert is_valid("AA") == True

def test_is_valid_11():
    assert is_valid("A2") == False

def test_is_valid_12():
    assert is_valid("2A") == False

def test_is_valid_13():
    assert is_valid("22") == False


def test_is_valid_14():
    assert is_valid(" 2") == False