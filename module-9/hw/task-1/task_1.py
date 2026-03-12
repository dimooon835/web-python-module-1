staff_data = [
    ("Employee", "Алиса", 2000),
    ("Manager", "Боб", 2500, 800),
    ("Sales", "Кира", 1800, 12000),
    ("Employee", "Данил", 2200),
    ("Sales", "Ева", 1700, 7000)
]


class Employee:
    # TODO: реализовать __init__(name, base_salary)
    # сохранить self.name и self.base_salary
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    # TODO: реализовать monthly_income()
    # вернуть доход за месяц обычного сотрудника: base_salary
    def monthly_income(self):
        return self.base_salary


class Manager(Employee):
    # TODO: реализовать __init__(name, base_salary, bonus)
    # вызвать super().__init__(...) и сохранить self.bonus
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    # TODO: переопределить monthly_income()
    # вернуть доход менеджера: base_salary + bonus
    def monthly_income(self):
        return self.base_salary + self.bonus


class Sales(Employee):
    # TODO: реализовать __init__(name, base_salary, sales_amount)
    # вызвать super().__init__(...) и сохранить self.sales_amount
    def __init__(self, name, base_salary, sales_amount):
        super().__init__(name, base_salary)
        self.sales_amount = sales_amount

    # TODO: переопределить monthly_income()
    # вернуть доход sales: base_salary + sales_amount * 0.05
    def monthly_income(self):
        return self.base_salary + self.sales_amount * 0.05


def calculate_total_income(staff):
    total = 0
    # TODO: пройти по staff и для каждого person добавить person.monthly_income() в total
    for person in staff:
        total += person.monthly_income()
    return total


staff = []
for row in staff_data:
    role = row[0]

    # TODO:
    # если role == "Employee": Employee(name, base_salary)
    # если role == "Manager": Manager(name, base_salary, bonus)
    # если role == "Sales": Sales(name, base_salary, sales_amount)
    # добавить созданный объект в staff
    if role == "Employee":
        staff.append(Employee(row[1], row[2]))
    elif role == "Manager":
        staff.append(Manager(row[1], row[2], row[3]))
    elif role == "Sales":
        staff.append(Sales(row[1], row[2], row[3]))


for person in staff:
    # TODO: вывести person.name и person.monthly_income()
    print(f"{person.name}: {person.monthly_income()}")

print("Общий фонд:", calculate_total_income(staff))