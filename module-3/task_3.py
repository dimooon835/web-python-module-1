# fruits = {"яблоко", "банан", "апельсин"}
# fruits.add("груша")
# fruits.update(["смородина", "клубника"])
# print(fruits)


# fruits = {"яблоко", "банан", "апельсин"}
# fruits.remove("яблоко")
# fruits.discard("груша")
# fruits.pop()
# print(fruits)


# my_set = {x for x in range(5)}
# print(my_set)


# set_a = {1, 2, 3, 4}
# set_b = {4, 5, 6, 7}
# result = set_a.union(set_b) # Метод
# result_operator = set_a | set_b # Оператор
# set_a |= set_b # Присвоение
# print(result, result_operator, set_a)


# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# result = set_a.intersection(set_b) # Метод
# result_operator = set_a & set_b # Оператор
# set_a &= set_b # Присвоение
# print(result, result_operator, set_a)


# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# result = set_a.difference(set_b) # Метод
# result_operator = set_a - set_b # Оператор
# set_a -= set_b # Присвоение
# print(result, result_operator, set_a)


# set_a = {1, 2, 3, 4}
# set_b = {3, 4, 5, 6}
# result = set_a.symmetric_difference(set_b) # Метод
# result_operator = set_a ^ set_b # Оператор
# set_a ^= set_b # Присвоение
# print(result, result_operator, set_a)


# my_set = {1, 2, 3}
# print(3 in my_set)
# print(5 not in my_set)
# print(len(my_set)) # Длина множества
# print(sum(my_set)) # Сумма множества
# print(min(my_set), max(my_set)) # Мин/макс число в множестве
# for num in my_set:
#     print(num)

# # 1
# fruits = ("яблоко", "банан", "яблоко")
# fruit = input("Введите фрукт: ")
# count = fruits.count(fruit)
# print(f"Фрукт встречается {count} раз")


# # 2
# fruits = ("banana", "apple", "bananamango", "mango", "strawberry-banana")
# fruit = input("Введите фрукт: ")
# count = 0
# for item in fruits:
#     if fruit in item:
#         count += 1
# print(f"Фрукт встречается {count} раз")


# # 3
# cars = ("audi", "opel", "lada", "opel")
# old_car = input("Введите название производителя для замены: ")
# new_car = input("Введите новое название производителя: ")
# result = []
# for item in cars:
#     if item == old_car:
#         result.append(new_car)
#     else:
#         result.append(item)
# result_tuple = tuple(result)
# print(f"Обновленный список производителей:", result_tuple)


# # 4
# numbers = (1, 220, 45, 254, 6, 9, -23)
# count = {}
# for num in numbers:
#     length = len(str(abs(num)))

#     if length in count:
#         count[length] += 1
#     else:
#         count[length] = 1

# for count, n in count.items():
#     print(f"{count} цифр - {n} элементов")


# # 4
# network = {
#     "Me": {"Alice", "Bob"},
#     "Alice": {"Me", "Cahrlie", "Bob"},
#     "Bob": {"Me", "David", "Eve"},
#     "Charlie": {"Alice"},
#     "David": {"Alice", "Bob"},
#     "Eve": {"Bob"},
# }
# user = "Me"
# friends_user = network[user]
# friends_friends = set()

# for friend in friends_user:
#     friends_friends.update(network)

# result = friends_friends - friends_user
# result.discard(user)
# print(result)


# # 5
# win_numbers = {4, 65, 35, 9, 49}
# print()
# user_numbers = set()