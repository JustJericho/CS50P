from numb3rs import validate

def test_validate():
    assert validate("0.0.0.0") == False
    assert validate("1.2.3.4") == True
    assert validate("11.22.33.44") == True
    assert validate("111.222.333.444") == False
    assert validate("abcdefghij") == False
    assert validate("abc.def.gh.i.j") == False