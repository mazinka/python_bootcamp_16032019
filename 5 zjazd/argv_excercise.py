'''

exapmle:
python argv_excercise.py dodaj 1 2
3
python argv_excercise.py mnóz 1 2
2
python argv_excercise.py odejmij 1 2
-
'''

import sys
print(sys.argv)
lista = sys.argv[1:]

lista =['dodaj','1','2']
if len(lista) != 3:
    raise ValueError("za malo lub za duzo argumentow")


dzialanie = lista[0]
a = int(lista[1])
b = int(lista[2])

if dzialanie[0] =="dodaj":
    wynik = a + b

elif dzialanie == 'odejmij':
    wynik = a - b

print(wynik)

