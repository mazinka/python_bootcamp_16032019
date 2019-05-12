
import sys
try:

    nazwa_pliku = sys.argv[1]
    with open(nazwa_pliku.txt) as f:
        for index, linia in enumerate(f, start=1):  # numeruje linie
            print(f'{index}: {linia}', end="")

except IndexError:
    print('nie podałeś nazwy pliku')



