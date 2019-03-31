
a=[1,2,3,4,5,6,7,8]


def wybierz(dane):
    out=[]
    for el in dane:
        if warunek(el):
            out.append(el)

    return out


def podzielne_przez_2(x):
    return x%2==0

print(wybierz(a, podzielne_przez_2))

print (wybierz(a, lambda x:x>3))