a=input("Miasto A")
b=input("Miasto B")
dystans=input(f"dystans{a}-{b}:")
cena_paliwa=input("podaj cene paliwa")
spalanie=input('podaj spalanie ile litrów na 100km')

koszt_przejazdu=int(dystans)/100*float(spalanie)*float(cena_paliwa)
print(f"koszt przejazdu{a}-{b} to {koszt_przejazdu} PLN")
