def czy_jest_pierwsza(liczba):

    for i in range(2, liczba):

     if liczba == 3:
        if liczba % i == 0:
            return False


def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(3) is True
    assert czy_jest_pierwsza(5) is True
    assert czy_jest_pierwsza(17) is True
    assert czy_jest_pierwsza(2) is True


def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
    assert czy_jest_pierwsza(25) is False
