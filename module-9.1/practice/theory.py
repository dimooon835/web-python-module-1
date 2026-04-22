# def parse(a, b):
#     try:
#         x = int(a)
#         y = int(b)
#         return x / y
#     except ValueError:
#         return "Ошибка a или b не число"
#     except ZeroDivisionError:
#         return "Делить на ноль нельзя"
    
# print(parse("10", "2"))
# print(parse("10", "0"))
# print(parse("abc", "2"))


# try:
#     data = {"name": "Alice"}
#     print(data{"email"})
# except KeyError as e:
#     print("Тип:", type(e).__name__)
#     print("Аргумент:", e.args)
#     print("Сообщение:", e)


# def set_discount(percent):
#     if not 0 <= percent <= 100:
#         raise ValueError("Скидка должна быть в диапазоне от 0 до 100")
#     return f"Скидка установлена: {percent}%"

# print(set_discount(20))
# print(set_discount(120))


# def load_user(data, user_id):
#     try:
#         return data[user_id]
#     except KeyError:
#         print(f"Пользователь не найден: {user_id}")
#         raise

# users = {1: "Alice"}
# try:
#     print(load_user(users, 2))
# except KeyError:
#     print("Ошибка")


# class ConfigError(Exception):
#     pass

# def load_port(raw_port):
#     try:
#         return int(raw_port)
#     except ValueError as e:
#         raise ConfigError("Поле PORT должно быть целым числом") from e
    
# try:
#     load_port("abc")
# except ConfigError as e:
#     print("Тип:", type(e).__name__)
#     print(type(e).__cause__)


# class EmployeeError(Exception):
#     pass

# class EmployeeNotFoundError(EmployeeError):
#     message2 = "Сотрудник не найден"
#     pass

# class SalaryValidationError(EmployeeError):
#     pass

# def find_employee(employees, emp_id):
#     if emp_id not in employees:
#         raise EmployeeNotFoundError(f"Сотрудник {emp_id} не найден")
#     return employees[emp_id]

# def validate_salary(value):
#     if value < 0:
#         raise SalaryValidationError("ЗП не может быть отрицательным")
    
# try:
#     find_employee({}, 10)
# except EmployeeNotFoundError as e:
#     print(e.message2)
# except SalaryValidationError as e:
#     print(e)


def normalize_percent(x):
    assert isinstance(x, int), "должен быть числом"
    if not 0 <= x <= 100:
        raise ValueError("Процент должен быть от 0 до 100")
    return x / 100

print(normalize_percent(25))
print(normalize_percent("abc"))