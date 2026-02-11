"""
ЗАДАЧА: Анализ чатов пользователей

Даны сообщения в чате. Каждое сообщение представлено словарём
со следующими ключами:
- "user"      : имя пользователя (строка)
- "text"      : текст сообщения (строка)
- "timestamp" : время сообщения (целое число, возрастает не строго)

Пример входных данных:
messages = [
    {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
    {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
    {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб",   "text": "пока",                  "timestamp": 20},
]

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Посчитать количество сообщений каждого пользователя.
   Результат сохранить в словарь вида:
   {
       "Алиса": 3,
       "Боб": 2
   }

2. Для каждого пользователя:
   2.1 Найти множество уникальных слов, которые он использовал
       (слова разделяются методом split()).
   2.2 Найти самое частое слово пользователя.
       Если самых частых слов несколько — можно выбрать любое.

3. Найти пользователя с самым большим словарным запасом,
   где словарный запас — это количество уникальных слов,
   использованных пользователем.

4. Найти множество слов, которые использовали ВСЕ пользователи
   (пересечение множеств слов пользователей).

5. Для каждого пользователя определить максимальный перерыв
   между его сообщениями:
   - перерыв = разница между timestamp текущего и предыдущего сообщения
   - найти пользователя с самым большим таким перерывом
"""

from collections import Counter

messages = [
    {"user": "Алиса", "text": "привет здравствуй",     "timestamp": 1},
    {"user": "Боб",   "text": "здравствуй",            "timestamp": 2},
    {"user": "Алиса", "text": "как дела у тебя",       "timestamp": 3},
    {"user": "Боб",   "text": "привет Алиса",          "timestamp": 4},
    {"user": "Алиса", "text": "привет привет здравствуй", "timestamp": 10},
    {"user": "Боб",   "text": "пока",                  "timestamp": 20},
]


user_message_count = {}
user_words = {}
user_timestamps = {}

for message in messages:
    user = message["user"]
    text = message["text"]
    timestamp = message["timestamp"]

    words = text.split()

    user_message_count[user] = user_message_count.get(user, 0) + 1
    
    if user not in user_words:
        user_words[user] = []
    user_words[user].extend(text.split())

    if user not in user_timestamps:
        user_timestamps[user] = []
    user_timestamps[user].append(timestamp)

unique_words = {}
most_common_words = {}

for user, words in user_words.items():
    unique = set(words)
    unique_words[user] = unique

    word = Counter(words)
    most_common_words[user] = word.most_common(1)[0][0]

top_words_user = max(unique_words, key = lambda user: len(unique_words[user]))

common_words = set.intersection(*unique_words.values()) if unique_words else set()

max_break = {}
for user, times in user_timestamps.items():
    times.sort()
    if len(times) < 2:
        max_break[user] = 0
    else:
        breaks = [int(times[i]) - int(times[i - 1]) for i in range(1, len(times))]
        max_break[user] = max(breaks)
    user_max_break = max(max_break, key = max_break.get)

print("1.", user_message_count)
print("2.1", unique_words)
print("2.2", most_common_words)
print("3.", top_words_user)
print("4.", common_words)
print("5.1", max_break)
print("5.2", user_max_break)