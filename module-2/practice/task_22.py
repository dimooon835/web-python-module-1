# # 1
# expression = input("Введите арифметическое выражение (например, 23+12): ")

# operations = ['+', '-', '*', '/']

# for op in operations:
#     if op in expression:
#         parts = expression.split(op)
        
#         num1 = float(parts[0].strip())
#         num2 = float(parts[1].strip())
        
#         if op == '+':
#             result = num1 + num2
#         elif op == '-':
#             result = num1 - num2
#         elif op == '*':
#             result = num1 * num2
#         elif op == '/':
#             if num2 != 0:
#                 result = num1 / num2
#             else:
#                 result = "Ошибка: деление на ноль"
        
#         print(f"Результат: {result}")
#         break
# else:
#     print("Ошибка: неверный формат выражения")

# 2
import random

list_size = 20
min_val = -10
max_val = 10
my_list = [random.randint(min_val, max_val) for _ in range(list_size)]

print(f"Исходный список: {my_list}")

minimum_element = min(my_list)
maximum_element = max(my_list)

negative_count = sum(1 for item in my_list if item < 0)
positive_count = sum(1 for item in my_list if item > 0)
zeros_count = sum(1 for item in my_list if item == 0)

print(f"Минимальный элемент: {minimum_element}")
print(f"Максимальный элемент: {maximum_element}")
print(f"Количество отрицательных элементов: {negative_count}")
print(f"Количество положительных элементов: {positive_count}")
print(f"Количество нулей: {zeros_count}")