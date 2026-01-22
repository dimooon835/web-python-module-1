# # 1
# word = input("Введите строку: ")
# reversed = word[::-1]
# print(reversed)

# # 2
# text = input("Введите строку: ")

# letters_count = 0
# digits_count = 0

# for char in text:
#     if char.isalpha():
#         letters_count += 1
#     elif char.isdigit():
#         digits_count += 1

# print(f"Кол-во букв: {letters_count}")
# print(f"Кол-во цфир: {digits_count}")

# # 3
# text = input("Введите текст: ")
# symbol = input("Введите символ для поиска: ")

# count = text.count(symbol)
# print(f"Символ {symbol} встречается {count} раз")

# # 4
# text = input("Введите строку: ")
# word = input("Введите слово: ")

# count = text.count(word)
# print(f"Слово {word} встречается {count} раз")

# # 5
# text = input("Введите строку: ")
# word = input("Введите слово: ")
# replace = input("Введите замену: ")

# result = text.replace(word, replace)

# print(result)


# # 1
# text = input("Введите текст: ")

# def process_text(text):
#     update_text = ". ".join(s.capitalize() for s in text.split("."))

#     digits_count = 0
#     punc_count = 0
#     excl_count = 0

#     for char in update_text:
#         if char.isdigit():
#             digits_count += 1
#         elif char in ".,!?:;":
#             punc_count += 1
#         elif char == "!":
#             excl_count += 1

#     return update_text, digits_count, punc_count, excl_count

# update_text, digits_count, punc_count, excl_count = process_text(text)

# print(update_text)
# print(f"Кол-во цифр {digits_count}")
# print(f"Кол-во знаков препинания {punc_count}")
# print(f"Кол-во восклицательных знаков {excl_count}")

# # 2
# num = input("Введите числа: ")
# search = input("Введите число для поиска: ")

# count = num.count(search)
# print(f"Число {search} встречается в списке {count} раз")

# # 3
# numbers = (input("Введите числа через пробел: "))
# num = numbers.split()

# for i in range(len(num)):
#     num[i] = int(num[i])

# total = sum(num)
# average = total / len(num)

# print(f"Сумма чисел: {total}")
# print(f"Средняя чисел: {average}")


# 1
text = input("Введите числа: ")
numbers = text.split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

def process_numbers(numbers):
    sum_negative = 0
    sum_even = 0
    sum_odd = 0
    index_3 = 1
    min_index = max_index = 0

    for num in numbers:
        if num < 0:
            sum_negative += num
        if num % 2 == 0:
            sum_even += num
        else: 
            sum_odd += num

    for i in range(0, len(numbers), 3):
        index_3 *= numbers[i]

    start = min(min_index, max_index)
    end = max(min_index, max_index)
    index = 1
    for i in range(start, end):
        index *= numbers[i]

    first_positive = -1
    last_positive = -1
    for i, num in enumerate(numbers):
        if num > 0:
            if first_positive == -1:
                first_positive = i
            last_positive = i
        
    if first_positive != -1 and last_positive != first_positive:
        sum_between = sum(numbers[first_positive+1:last_positive])
    else:
        sum_between = 0

    return sum_negative, sum_even, sum_odd, index_3, index, sum_between

sum_negative, sum_even, sum_odd, index_3, index, sum_between = process_numbers(numbers)

print(sum_negative)
print(sum_even)
print(sum_odd)
print(index_3)
print(index)
print(sum_between)