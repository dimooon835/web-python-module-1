from abc import ABC, abstractmethod

# class Employee:
#     pass

# e = Employee()
# print(type(e))

class EmployeeBase(ABC):
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def compensation(self):
        pass

class Employee(EmployeeBase):
    company = "123123"

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary


    # def info(self):
    #     return f"{self.name} => {self.salary}"
    

    # @classmethod
    # def from_string(cls, raw):
    #     emp_id, name, salary = raw.split(",")
    #     return cls(int(emp_id), name, int(salary))
    

    # @staticmethod
    # def valid_name(name):
    #     return len(name.strip()) >= 2
    

    # def get_salary(self):
    #     return self.salary
    
    # def set_salary(self, value):
    #     if value < 0:
    #         self.salary = 0
    #     else:
    #         self.salary = value


    # def get_salary(self):

    # def set_salary(self, value):

    # @property
    # def salary(self):
    #     return self.salary
    
    # @salary.setter
    # def salary(self, value):
    #     self._salary = value

    # @salary.deleter
    # def salary(self):
    #     self._salary = 0


    def __str__(self):
        return f"{self.name}: {self.salary}"
    

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.emp_id == other.emp_id


    def __lt__(self, other):
        if not isinstance(other, Employee):
            return NotImplemented
        return self.emp_id < other.emp_id

    def yearly_income(self):
        return self.salary * 12
    

    def compensation(self):
        return self.salary

class LoggableMixIn:
    def log(self, message):
        print(f"[LOG] {self.name}: {message}")

class Manager(Employee, LoggableMixIn):
    def __init__(self, emp_id, name, salary, bonus):
        super().__init__(emp_id, name, salary)
        self.bonus = bonus

    def yearly_income(self):
        return super().yearly_income() + self.bonus


# e = Employee(1, "Alice", 2000)
# print(e.name, e.salary, Employee.company)


# print(e.info())


# e = Employee.from_string("2,Andrey,3000")
# print(e.emp_id, e.name, e.salary)


# e = Employee.from_string("2,Andrey,3000")
# print(e.emp_id, e.name, e.salary, Employee.valid_name(e.name))


# e = Employee.from_string("2,Andrey,3000")
# e.set_salary(4000)
# print(e.get_salary())


# e = Employee.from_string("2,Andrey,3000")
# e.salary = 4000
# print(e.salary)
# del e.salary
# print(e.salary)


# m = Manager(3, "Alexey", 2000, 5000)
# # print(m.yearly_income())
# print(Manager.__mro__)


# m = Manager(3, "Alexey", 2000, 5000)
# print(m.log("123123"))


# m = Manager(3, "Alexey", 2000, 5000)
# print(m)


m = Manager(3, "Alexey", 2000, 5000)
m1 = Manager(4, "Alice", 1000, 2000)
print(m == m1)
print(m < m1)
print(m1 < m)