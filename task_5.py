const_hour = 40

class Employee:
    def __init__(self, name, pin, hour) -> None:
        self.name = name
        self.pin = pin
        self.hour = hour

    def calc_salary(self):
        pass

    def total_salary(self):
        pass

    def calc_perfomance(self):
        return (self.hour * 100) / const_hour


class Manager(Employee):
    def __init__(self, name, pin, hour, salary) -> None:
        super().__init__(name, pin, hour)
        self.salary = salary

    def calc_salary(self):
        return self.salary


class Secretary(Employee):
    def __init__(self, name, pin, hour, salary) -> None:
        super().__init__(name, pin, hour)
        self.salary = salary

    def calc_salary(self):
        return self.salary


class SalesPerson(Employee):
    def __init__(self, name, pin, hour, sell_count, salary) -> None:
        super().__init__(name, pin, hour)
        self.sell_count = sell_count
        self.salary = salary

    def calc_salary(self):
        return self.salary + (self.sell_count * 50)


class CexEmployee(Employee):
    def __init__(self, name, pin, hour) -> None:
        super().__init__(name, pin, hour)

    def calc_salary(self):
        self.salary = self.hour * 100
        return self.salary


class SecretaryZamena(Employee):
    def __init__(self, name, pin, hour) -> None:
        super().__init__(name, pin, hour)

    def calc_salary(self):
        self.salary = self.hour * 100
        return self.salary


manager = Manager(
    "Барсбек Канаткулов",
    1,
    18,
    45000
)
secretary = Secretary(
    "Алымкул Тилекбаев",
    2,
    38,
    20000
)
sales_person = SalesPerson(
    "Айпери Шалымбекова",
    3,
    38,
    20,
    20000
)
cex = CexEmployee(
    "Бакыт Рустамов",
    4,
    25
)
cex2 = CexEmployee(
    "Алтынай Ширинбаева",
    5,
    40
)
zamena = SecretaryZamena(
    "Жанар Рыскулов",
    6,
    33
)
personal = [
    manager,
    secretary,
    sales_person,
    cex,
    cex2,
    zamena
]


def spend_comp_money():
    total_money = sum([
        person.calc_salary() for person in personal
    ])
    return f"Общий заработок персонала - {total_money}"


def print_info():
    total = spend_comp_money()
    for person in personal:
        print(
            f"ID - {person.pin}, "
            f"Name - {person.name} ,"
            f"Salary - {person.salary} ,"
            f"Performance - {person.calc_perfomance()}",
            end="\n"
        )
    return total


print_info()
print(spend_comp_money())




