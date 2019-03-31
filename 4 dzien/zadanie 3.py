def policz_znaki(tekst, start="<", end=">"):
    licznik = 0
    poziom=0

    for el in tekst:
        if el == end:
            poziom -= 1
        elif el == start:
            poziom +=1
        else:
            licznik += poziom
    return licznik



def test_ile_znakow_miedzy_nawiasami():
    assert policz_znaki('') == 0

def test_ile_znakow_w_napisie_bez_znacznikow():
    assert policz_znaki('ale ma kota') == 0

def test_ile_znakow_w_napisie_z_1_poziomem():
    assert policz_znaki('ale <ma> kota') == 2

def test_policz_znaki_wiele_poziomow_zaglebienia():
    assert policz_znaki('ala<m<a>>kota') == 3

def test_policz_znaki_inne_znaczniki():
    assert policz_znaki('ala [m[a]] kota','[',']') == 3


