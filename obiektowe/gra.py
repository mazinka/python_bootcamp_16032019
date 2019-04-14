import random

class Postac():

    def __init__(self, imie, atak, obrona, energia):

        self.imie = imie
        self._atak = atak  # właściwosci juz bardzo określone
        self._obrona = obrona
        self.energia = energia
        self.ekwipunek = []

    @classmethod #zeby nie dotyczylo wszystkiego calego obiektu tylko wybranego czegos
    def losowa_postac(cls):
        imie = random.choice (['adam', 'izydor', 'rufus','jeremiasz','flaneli'])
        atak = random.uniform(5,12)
        obrona = random.uniform(5,12)
        energia = random.uniform(20,120)
        return Postac(imie, atak, obrona, energia)

    @staticomethod
    def porownaj_postaci(postac1,postac2):
        if postac1.atak < postac2.atak:
            postac1, postac2 = postac2, postac1
        print(f'postac{postac1} jest silniejsza od {postac2}')


    def przedstaw_sie(self):
        print(f"jestem {self.imie}, mam {self.atak} ataków, {self.obrona} obrony i {self.energia} życia")

    def __str__(self):
        return f'{self.imie}({self.atak}/{self.obrona}}'

    @property
    def atak(self):
        atak = self._atak
        for przedmiot in self.ekwipunek:
            atak += przedmiot.bonus_do_ataku
        return atak

    @property
    def obrona(self):
        obrona = self._obrona
        for przedmiot in self.ekwipunek:
            obrona += przedmiot.bonus_do_obrony
        return obrona

    def daj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def uderz(self, postac2):
        obrazenia = self.atak - postac2.obrona
        obrazenia *=  round(random.uniform(0.5,1),2)
        if obrazenia > 0:
            postac2.energia -= obrazenia
            print(f"{self.imie} zadaje cios za {obrazenia:.2f} punktów")

    def czy_zyje(self):
        if self.energia <= 0:
            return False
        else:
            return True


    def walka(self, postac2):
        print("do walki staja:")
        self.przedstaw_sie()
        postac2.przedstaw_sie()

        print("niech rozpocznie sie walka!")




        while True:
            # self uderza postac2
            self.uderz(postac2)

            # spr czy postac 2 zyje

            if postac2.energia <= 0:
                print(f"{self.imie} wygrywa z {postac2.imie}")
                break

            # postac 2 uderza self
            postac2.uderz(self)

            # sprawdz czy self zyje
            if not self.czy_zyje():
                print(f'{postac2.imie} wygrywa z {self.imie}')
                break

class Przedmiot():

    def __init__(self, nazwa, bonus_do_ataku, bonus_do_obrony):
        self.nazwa = nazwa
        self.bonus_do_ataku = bonus_do_ataku
        self.bonus_do_obrony = bonus_do_obrony


class TestPostac():
    def test_postac_initialization(self):
        postac = Postac("Albert", atak=10, obrona=15, energia=100)
        assert postac.imie == "Albert"
        assert postac.atak == 10
        assert postac.obrona == 15
        assert postac.energia == 100
        assert postac.ekwipunek == []

    def test_postac_przedstaw_sie(self, capsys):
        postac = Postac("Albert", atak=10, obrona=15, energia=100)
        postac.przedstaw_sie()
        captured = capsys.readouterr()
        assert captured.out == "jestem Albert, mam 10 ataków, 15 obrony i 100 życia\n"

    def test_postac_czy_zyje(self):
        postac = Postac("Albert", atak=10, obrona=15, energia=100)
        assert postac_czy_zyje()
        postac.energia = 0
        assert postac_czy_zyje() == False
        postac.energia = -1
        assert postac_czy_zyje() == False


    def test_porownanie_postaci(self, capsys):
        albert = Postac("Albert", atak=17, obrona=15, energia=100)
        teodor = Postac("Teodor", atak=22, obrona=11, energia=110)
        Postac.porownaj_postaci(albert, teodor)
        captured = capsys.readouterr()
        assert captured.out == "postac teodor jest silniejsza niz albert\n"

class TestPrzedmiot():
    def test_przedmiot_initialization(self):
        przedmiot = Przedmiot("siekiera", 20, 5)
        assert przedmiot.nazwa == "siekiera"
        assert przedmiot.bonus_do_ataku == 20
        assert przedmiot.bonus_do_obrony == 5

    def test_postac_daj_przedmiot(self):
        postac = Postac("Albert", atak=10, obrona=15, energia=100)
        przedmiot = Przedmiot("siekiera", 20, 5)
        assert len(postac.ekwipunek) == 0
        postac.daj_przedmiot(przedmiot)
        assert len(postac.ekwipunek) == 1
        postac.przedstaw_sie()
        captured = capsys.readouterr()
        assert captured.out == "jestem Albert, mam 30 ataków, 20 obrony i 100 życia\n"


if __name__ == "__main__":
    albert = Postac("Albert", atak=12, obrona=15, energia=100)
    teodor = Postac("Teodor", atak=16, obrona=11, energia=110)
    print('w grze uczestnicza: albert, teodor)'
    siekiera = Przedmiot("siekiera", 20, 5)
    albert.daj_przedmiot(siekiera)
    albert.walka(teodor)

    for _ in range(12):
        Postac.losowa_postac().przedstaw_sie()