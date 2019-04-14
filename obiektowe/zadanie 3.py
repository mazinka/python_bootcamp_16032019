class ElectricCar:


    def __init__(self, max_range):
        self.max_range = max_range
        self.traveled_distance = 0


    def drive(self, distance):
        if self.traveled_distance + distance > self.max_range:
            to_travel = self.max_range - self.traveled_distance
            self.traveled_distance = self.max_range
            return to_travel
        else:
            self.traveled_distance += distance
    return distance


    def charge(self):
        self.traveled_distance = 0


class TestElectricCar:

    def test_1_przejazd(self):
        car = ElectricCar(120)
        assert car.max_range == 120
        assert car, traveled_distance == 0

    def test_car_drive(self):
        car = ElectricCar(100)
        assert car.drive(70) == 70
        assert car.traveled_distance == 70
        assert car.drive(50) == 30
        assert car.traveled_distance == 100
        assert car.drive(10) == 0
        assert car.traveled_distance == 100

    def test_electric_car_charge(self):
        car = ElectricCar(100)
        assert car.drive(120) == 100
        assert car.drive(10) == 0
        car.charge()
        assert car.drive(120)
