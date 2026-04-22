from abc import ABC, abstractmethod

staff_rows = [
    ("Developer", "Алиса", 2200, "Engineering", 12, 25),
    ("Manager", "Боб", 2800, "Engineering", 900),
    ("Analyst", "Кира", 2000, "Data", 14, 40),
    ("Developer", "Данил", 2400, "Engineering", 4, 25),
    ("Manager", "Ева", 2600, "Data", 600),
    ("Analyst", "Жан", 1900, "Operations", 20, 30),
]


class EmployeeBase(ABC):
    # TODO: __init__(name, base_salary, department)
    def __init__(self, name, base_salary, department):
        self.name = name
        self.base_salary = base_salary
        self.department = department
    # TODO: short() -> строка "Имя (Department)"
    def short(self):
        return f"{self.name} ({self.department})"

    @abstractmethod
    def total_pay(self):
        return self.total_pay

    # TODO: __repr__
    def __repr__(self):
        return f"{self.__class__.__name__}(name = '{self.name}', total = {self.total_pay()})"
    # TODO: __lt__(other) -> сравнение по total_pay()
    def __lt__(self, other):
        return self.total_pay() < other.total_pay()


class Developer(EmployeeBase):
    # TODO: __init__(name, base_salary, department, overtime_hours, overtime_rate)
    def __init__(self, name, base_salary, department, overtime_hours, overtime_rate):
        super().__init__(name, base_salary, department)
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate
    # TODO: total_pay()
    def total_pay(self):
        return self.base_salary + (self.overtime_hours * self.overtime_rate)


class Manager(EmployeeBase):
    # TODO: __init__(name, base_salary, department, bonus)
    def __init__(self, name, base_salary, department, bonus):
        super().__init__(name, base_salary, department)
        self.bonus = bonus
    # TODO: total_pay()
    def total_pay(self):
        return self.base_salary + self.bonus


class Analyst(EmployeeBase):
    # TODO: __init__(name, base_salary, department, reports_done, report_rate)
    def __init__(self, name, base_salary, department, reports_done, report_rate):
        super().__init__(name, base_salary, department)
        self.reports_done = reports_done
        self.report_rate = report_rate
    # TODO: total_pay()
    def total_pay(self):
        return self.base_salary + (self.reports_done * self.report_rate)


class DepartmentBudget:
    # TODO: __init__(department_name)
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []
    # TODO: add_employee(emp)
    def add_empolyee(self, emp):
        self.employees.append(emp)
    # TODO: department_total()
    def department_total(self):
        return sum(emp.total_pay() for emp in self.employees)
    # TODO: top_paid()
    def top_paid(self):
        return max(self.employees) if self.employees else None


class PayrollService:
    # TODO: __init__(employees)
    def __init__(self, employees):
        self.employees = employees
    # TODO: total_company_payroll()
    def total_company_payroll(self):
        # for emp in self.employees:
        #     print(f"Checking {emp.name}: {emp.total_pay()}")
        return sum(emp.total_pay() for emp in self.employees)
    # TODO: totals_by_department()
    def totals_by_department(self):
        totals = {}
        for emp in self.employees:
            totals[emp.department] = totals.get(emp.department, 0) + emp.total_pay()
        return totals
    # TODO: highest_paid_employee()
    def highest_paid_employee(self):
        return max(self.employees)


# TODO: создать объекты сотрудников из staff_rows
staff_objects = []
for row in staff_rows:
    role, name, salary, dep = row[0], row[1], row[2], row[3]
    if role == "Developer":
        staff_objects.append(Developer(name, salary, dep, row[4], row[5]))
    elif role == "Manager":
        staff_objects.append(Manager(name, salary, dep, row[4]))
    elif role == "Analyst":
        staff_objects.append(Analyst(name, salary, dep, row[4], row[5]))
# TODO: создать PayrollService и вывести общий payroll
payroll = PayrollService(staff_objects)
print(f"\nОбщий фонд выплат: {payroll.total_company_payroll()}")
# TODO: вывести суммы по отделам
print(f"\nВыплаты по отделам: ")
dept_totals = payroll.totals_by_department()
for dept, amount in dept_totals.items():
    print(f"{dept}: {amount}")
# TODO: вывести самого высокооплачиваемого сотрудника
top_emp = payroll.highest_paid_employee()
print(f"\nСамый дорогой сотрудник: {top_emp.short()} - {top_emp.total_pay()}\n")