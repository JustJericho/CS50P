from twttr import shorten

def test_shorten_logic():
    assert shorten("aeiou/AEIOU") == "/"
def test_shorten_numeric():
    assert shorten("143242") == "143242"
def test_shorten_upper():
    assert shorten("cycling") == "cyclng"
def test_shorten_punc():
    assert shorten("....") == "...."
