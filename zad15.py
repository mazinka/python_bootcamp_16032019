from random import randint


gracz_x=randint(1, 10)
gracz_y=randint(1, 10)
skarb_x=randint(1, 10)
skarb_y=randint(1, 10)


liczba_ruchow=0
minimalna_liczba_ruchow=abs(skarb_x-gracz_x)+abs(skarb_y-gracz_y)
print('minimalna liczba ruchow', minimalna_liczba_ruchow)

while True:
    kierunek = input("podaj kierunek [w,a,s,d]")
    odleglosc_przed_ruchem = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    if kierunek == "w":
        gracz_y += 1
    elif kierunek == "s":
        gracz_y -= 1
    elif kierunek == "a":
        gracz_x -= 1
    elif kierunek == "d":
        gracz_x += 1

    liczba_ruchow +=1
    if liczba_ruchow>=2*minimalna_liczba_ruchow:
        skarb_x=randint(1, 10)
        skarb_y=randint(1, 10)

        liczba_ruchow=0
        minimalna_liczba_ruchow=abs(skarb_x-gracz_x)+abs(skarb_y-gracz_y)
        print('jestes gamon, skarb zmienil polozenie')

    odleglosc_po_ruchu = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)

    if randint(1, 5)!=5:
        [rint(f"twoja pozycja to")]

    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print("wyszedłeś poza plansze")
        break
    if odleglosc_po_ruchu < odleglosc_przed_ruchem:
        print('cieplo')
    else:
        print('zimno')

    print(f"twoja pozycja to x={gracz_x}, y={gracz_y}")

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print('brawo znalazles skarb')
        break
