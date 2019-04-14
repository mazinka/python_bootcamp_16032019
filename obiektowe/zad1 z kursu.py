class Product():

    def __init__(self, numer, nazwa, cena):

        self.numer = numer
        self.nazwa = nazwa
        self.cena = cena

    def print_info(self):
        print(f"numer z katalogu:
        {self.numer}"", nazwa produktu:
        {self.nazwa}, cena produktu:
        {self.cena}, "dziekujemy za zakupy")


product=Product(1, "woda", 10.99)
product=print_infor()

product2 = Product(2, "piwo", 5.99)
product2 = print_infor()

def test_Product():
    product=Product(1, "woda", 10.99)
    assert product.numer==1
    assert produkt.nazwa=='woda'
    assert produkt.cena==10.99

def test_Product_product_info(capsys):
    product=Product(1, "woda", 10.99)
    product.print_infor()
    captured = capsys.readouterr()

    assert captured.out=='product "woda, numer: 1, cena: 10.99 PLN\n'

