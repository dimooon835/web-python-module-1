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


# 1
text = input("Введите текст: ")

update_text = ". ".join(s.capitalize() for s in text.split("."))

print(update_text)


# 2
