word = input("Введите слово: ")
d = {}
for sym in word:
    d.setdefault(sym, 0)
    d[sym] += 1

for symbol, count in d.items():
    print(f"{symbol}={count}")