# # 1
# def is_palindrome(s):
#     s = s.lower().replace(" ", "")
    
#     return s == s[::-1]

# text = input("Введите строку: ")

# if is_palindrome(text):
#     print("Введённая строка является палиндромом")
# else:
#     print("Введённая строка не является палиндромом")

# # 2
# text = input("Введите текст: ")

# reserved_words = input("Введите зарезервированные слова через пробел: ").split()

# words = text.split()

# for i in range(len(words)):
#     if words[i].lower() in [word.lower() for word in reserved_words]:
#         words[i] = words[i].upper()

# result = ' '.join(words)

# print("Измененный текст:")
# print(result)

# 3
def count_sentences(text):
    sentences = text.split('.')
    
    sentences = [s.strip() for s in sentences if s.strip()]
    
    return len(sentences)

text = input("Введите текст: ")
sentence_count = count_sentences(text)
print(f"В тексте {sentence_count} предложений")