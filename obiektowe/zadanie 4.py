class Basket:

    def __init__(self):
        self.entries = []

    def add_product(self, product, number):
        for entry in self.entries:
            if entry.product == product:
                entry.number += number
                return
        self.entries.append(BasketEntry(product, number))


    def count_total_price(self):
        total = 0
        for entry in self.entries:
            total +=entry.entry_price()
        return total
        #return sum(e.entry_price () for e in self.entries

    def generate_report(self):
        result ="produkt w koszyku:\n"
        for el in self.entries:
           result += f'{el.product.name}, cena: {el.product.price: .2f}*{el.number}'
        result += f" w sumie: {self.count_total_price()}"
        return result

class BasketEntry:
    def __init__(self, product, number):
        self.product = product
        self.number = number



    def entry_price(self):
        return self.product.price * self.number


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


def test_basket_init():
    b = Basket()


def test_product_init():
    p = Product(1, "woda", 10.00)
    assert p.id == 1
    assert p.name == 'woda'
    assert p.price == 10.00


def test_BasketEnty_init():
    p = Product(1, "woda", 10.00)
    be = BasketEntry(p, 5)
    assert be.product == p
    assert be.number == 5


def test_add_product_to_basket():
    b = Basket()
    p = Product(1, "woda", 10.00)
    b.add_product(p, 5)
    assert b.count_total_price() == 50

def test_add_product_to_basket():
    b = Basket()
    p = Product(1, "woda", 10.00)
    b.add_product(p, 4)
    b.add_product(p, 1)
    assert b.count_total_price() == 50
    assert b.generate_report() =="""produkt w koszyku:
woda(1), cena: 10.00x5, w sumie: 50.00"""