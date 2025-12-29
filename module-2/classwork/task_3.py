prices = {"bread": 20, "milk": 80, "cheese": 25}
cart = {"bread": 2, "cola": 1, "milk": 3}
d = {}
total = 0
for key, value in cart.items():
    if key in prices:
        total += prices[key] * value
    else:
        print(f"Товар {key} отсутствует в списке")
print(f"Итоговая стоимость: {total}")