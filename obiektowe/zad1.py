class Pies:
    #atrybuty klasowe
    liczba_nog=4 #atrybut cechy
    gatunek='canis canis'


    def_init_(self,imie, wiek, rasa, wiek): #to jest zwykła funkcja
        #atrybuty instacji
        self.imie=imie
        self.rasa=rasa
        self.wiek=wiek
        self.usposobienie="przyjacielski"

    def ludzki_wiek(self): #self zwraca do każdej cechy
        return self.wiek*
    #metoda instacji
azor=Pies('azor', 'kundel', 10) #instancja klasy pies
reksio=Pies()#instancja klasy pies
print(azor)


azor.imie="azor"
azor.rasa="kundel"
reksio.imie='Rex'
reksio.rasa="owczarek"

azor.wiek=4
print(azor.liczba_nog)
print(reksio.liczba_nog)
print(reksio.gatunek)
print(azor.ludzki_wiek)

print(azor.ludzki_wiek())