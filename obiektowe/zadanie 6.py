class Employee():

    def __init__(self, first_name, last_name, rate_per_hour=100):
        self.first_name = first_name
        self.last_name = last_name
        self.rate_per_hour = rate_per_hour
        self.worked_hours = 0


    def register_time(self, hours):
        self.worked_hours = hours

    def pay_salary(self):
        if self.worked_hours > 8:
            to_pay = 8*self.worked_hours +(self.worked_hours-8)* 2*self.rate_per_hour
        else:
            to_pay=self.worked_hours*self.rate_per_hour
        self.worked_hours = 0
        return to_pay


class PremiumEmployee(Employee):
    def __init__(self, first_name, last_name, rate_per_hour=100): #odwołujemy się do głównego kontruktora
        super().__init__(first_name, last_name, rate_per_hour=100) #działa jak self ale nie przesłania niczego
        self.bonuses = 0


    def give_bonuses(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        to_pay = super().pay_salary()
        to_pay += self.bonuses
        self.bonuses = 0
        return to_pay

def test_employee_initialization():
    employee = Employee("Jan", "Nowak", 100.0)
    assert employee.first_name == "Jan"
    assert employee.last_name == "Nowak"
    assert employee.rate_per_hour == 100.0


def test_employee_register_time():
    employee = Employee("Jan", "Nowak", 100.0)
    assert employee.worked_hours == 0
    employee.register_time(5)
    assert employee.worked_hours == 5


def test_pay_salary():
    employee = Employee("Jan", "Nowak", 100.0)
    assert employee.pay_salary() == 0
    employee.register_time(12)
    assert employee.pay_salary() == 1200

def test_premium_employee_init():
    employee = PremiumEmployee ("james", 'bond', 100.0)
    assert employee.bonuses == 0
    employee.give.bonus(1000.0)
    assert employee.bonuses == 1000.0

def test_premium_employee_pay():
    employee = PremiumEmployee ("james", 'bond', 100.0)
    elployee .register_time(5)
    employee.give.bonus(1000.0)
    assert employee.pay_salary() ==1000
