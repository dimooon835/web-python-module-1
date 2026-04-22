# text = "Python"


# print(text.swapcase())
# print(text.upper())
# print(text.lower())
# print(text.capitalize())


# print(text.find("p"))
# print(text.index("j"))


# print(text.replace("Python", "213", 1))


# print("Только буквы: ", text.isalpha())
# print("Только цифры: ", text.isdigit())
# print("Буквы и цифры: ", text.isalnum())
# print("Пробелы: ", text.isspace())
# print("Заглавные: ", text.isupper())
# print("Прописные: ", text.islower())


# print(text.strip()) # Очистка с левой и правой части
# print(text.lstrip()) # Очистка левой части
# print(text.rstrip()) # Очистка правой части


# sl = text.splitlines() # "row_1\nrow_2\nrow_3"
# print(sl)
# f = text.split(", ") # Если пусто, то разбиение по пробелам
# # print(f)
# u = ", ".join(f) # Объединение элементов в строку
# # print(f, u)


# tuple_1 = (1,2,3)
# tuple_2 = tuple([1,2,3])
# tuple_3 = 1,2,3

# print(tuple_1)
# print(tuple_2)
# print(tuple_3)


# tuple_1 = tuple(range(0, 11))
# print(tuple_1[0])
# print(tuple_1[2:5])


# num1, * other, last_el = tuple(range(0, 11))
# print(num1, other, last_el)


# num1, _, num3, num4 = (1,2,3,4)
# print(num1, _, num3, num4)


# tuple1 = (1,2)
# tuple2 = (3,4)
# result = tuple1 + tuple2
# print(result)


# pattern = ("a", "b")
# repeated = pattern * 2
# print(repeated)


# f = ("apple", "banana")
# print("apple" in f)


# numbers = (1,2,3,2,4,5,2)
# print(numbers.count(2)) # Считаем кол-во
# print(numbers.index(2)) # Индекс первого вхождения поиска


# num_tuple = tuple(range(0, 5))
# for num in num_tuple:
#     print(num)

# for index, num in enumerate(num_tuple):
#     print(index, num)


tuple_1_sym = ("b")
tuple_2_sym = ("b",)
print(tuple_1_sym, tuple_2_sym)