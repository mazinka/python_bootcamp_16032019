def plaska_lista(lista):
    rezultat = []
    lista = [1, 2, [3, 4, 5]]

    for el in lista:
        if isinstance(el,list):
            for e in splaszcz(el):
                rezultat.append(e)

            return splaszcz (el)



    return rezultat





def test_pusta_lista():
    assert splaszcz([])== []

def test_pusta_lista():
    assert splaszcz([1,2,3])== [1,2,3]

def test_pusta_lista():
    assert splaszcz([1,2,[3,4,5]])== [1,2,3,4,5]