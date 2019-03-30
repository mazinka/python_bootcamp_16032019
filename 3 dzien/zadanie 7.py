napis=input("podaj napis:")


#SAMOGLOSKI=["a","o","e","u","i","y"]
SAMOGLOSKI="aeiouy"
licznik=0

for litera in napis.lower():  #zamienia na małe literki
    if litera.lower() in SAMOGLOSKI:
        licznik+=1

print(f'w tekscie: {napis} znajduje sie {licznik} samoglosek')


