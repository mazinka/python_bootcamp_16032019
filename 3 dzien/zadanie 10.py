liczniki={}
tekst=input('wpisz tekst')


for znak in tekst:
   liczniki[znak] = liczniki.get(znak,0) + 1
print(liczniki)