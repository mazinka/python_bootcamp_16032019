def silnia(a):
    a1 = a + 1
    print(a)
    if a == 0:
        print(1)
        return 1
    else:
        return a*silnia(a-1)



def test_jak_zero():
    assert silnia(0) == 1
def test_jak_wysoka_silnia():
    assert silnia(2)==2


def rekuprint(lista):
    if len(lista)==1
        print(lista[0])
    else:
        print(lista[0])
        rekuprint(lista[1:])
lista[10,20,30,40]
rekuprint(lista)