import random

list1 = [random.randint(1, 100) for _ in range(10)]
list2 = [random.randint(1, 100) for _ in range(10)]

print("Первый список:", list1)
print("Второй список:", list2)

combined_list = list1 + list2
print("Объединенный список:", combined_list)

unique_combined = list(set(list1 + list2))
print("Объединенный без повторов:", unique_combined)

common_elements = list(set(list1) & set(list2))
print("Общие элементы:", common_elements)

unique_elements = list(set(list1).symmetric_difference(set(list2)))
print("Уникальные элементы:", unique_elements)

min_max_list = [min(list1), max(list1)] + [min(list2), max(list2)]
print("Минимальные и максимальные значения:", min_max_list)