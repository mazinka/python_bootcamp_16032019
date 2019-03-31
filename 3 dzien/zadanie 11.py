unikalna_liczba = set()

while True:
    dana = input("podaj liczbe:")
    if dana == 'k':
        break
  #  unikalna_liczba.add(int(dana))
    unikalna_liczba={int(el) for el in dane.split(",")}


print(f'unikalna liczba:{len(unikalna_liczba)}')
print(f'z czego parzystych w przedziale jest: {len(unikalna_liczba&set(range(0,101,2)))}')

