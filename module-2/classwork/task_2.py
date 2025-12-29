num = int(input("Ввести кол-во пар ключей: "))
d = {}
for num in range(num):
    key = input()
    value = input()
    d.setdefault(key, value)
print(d)