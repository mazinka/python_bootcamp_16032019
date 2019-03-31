lista=[9,1,6,8,4,3,2,0]


for i in range(len(lista)):

    indeks_min_wartosci = i
    for j in range(i, len(lista)):
        if lista[j] < lista[indeks_min_wartosci]:
            indeks_min_wartosci=j
    lista[i], lista[indeks_min_wartosci]=lista[indeks_min_wartosci],lista [i]


assert lista==[0,1,2,3,4,6,8,9]

