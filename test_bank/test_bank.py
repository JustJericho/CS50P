from bank import value

def test_value_1():
    assert value("hi") == 20

def test_value_2():
    assert value("Hello") == 0