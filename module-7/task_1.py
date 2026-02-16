"""
ЗАДАЧА: Учёт инвентаря на складе

Формат строки:
дата,товар,тип,количество

Операции:
2024-01-01,яблоко,IN,50
2024-01-02,банан,IN,30
2024-01-03,яблоко,OUT,10
2024-01-03,груша,OUT,5
2024-01-04,груша,IN,20
2024-01-05,банан,OUT,40
2024-01-06,яблоко,OUT,5

Типы операций:
- IN  : поступление товара
- OUT : отгрузка товара

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Создать файл inventory.txt с операциями склада

2. Прочитать файл и загрузить все операции.

3. Для каждого товара:
   - посчитать итоговое количество на складе
   - посчитать общее количество поступивших единиц
   - посчитать общее количество отгруженных единиц

4. Найти товары:
   - у которых итоговое количество < 0 (ошибка учёта)
   - которые ни разу не поступали, но отгружались

5. Найти товар с:
   - максимальным количеством поступлений
   - максимальным количеством отгрузок

6. Сформировать множество всех дат,
   когда происходили операции с товаром "яблоко".

7. Записать подробный отчёт в файл report.txt.

- ОТЧЁТ ПО СКЛАДУ
- Итоговые остатки
- Общее поступление
- Общая отгрузка
- Товары с отрицательным остатком:
- Товары без поступлений, но с отгрузкой:
- Товар с максимальным поступлением:
- Товар с максимальной отгрузкой:
- Даты операций с яблоком:
"""


with open("inventory.txt", "w", encoding = "utf-8") as f:
   operations = [
      "2024-01-01,яблоко,IN,50",
      "2024-01-02,банан,IN,30",
      "2024-01-03,яблоко,OUT,10",
      "2024-01-03,груша,OUT,5",
      "2024-01-04,груша,IN,20",
      "2024-01-05,банан,OUT,40",
      "2024-01-06,яблоко,OUT,5"
   ]
   for op in operations:
      f.write(op + "\n")

data = []
inventory = {}
apple_dates = set()

with open("inventory.txt", "r", encoding = "utf-8") as f:
   for line in f:
      parts = [p.strip() for p in line.split(",")]
      if len(parts) == 4:
         date, product, operation_type, quantity = parts
         qty = int(quantity) if quantity.isdigit() else 0
         data.append({
            "date": date,
            "production": product,
            "operation_type": operation_type,
            "quantity": quantity
         })

         if product not in inventory:
            inventory[product] = {"in": 0, "out": 0}
         
         if operation_type == "IN":
            inventory[product]["in"] += qty
         elif operation_type == "OUT":
            inventory[product]["out"] += qty

         if product == "яблоко":
            apple_dates.add(date)

neg_balance = []
never_in = []
max_in_value = -1
max_in_item = ""
max_out_value = -1
max_out_item = ""

for product, stats in inventory.items():
   total = stats["in"] - stats["out"]

   if total < 0: neg_balance.append(product)
   if stats["in"] == 0 and stats["out"] > 0: never_in(product)

   if stats["in"] > max_in_value:
      max_in_value = stats["in"]
      max_in_item = product
   if stats["out"] > max_out_value:
      max_out_value = stats["out"]
      max_out_item = product

with open("report.txt", "w", encoding = "utf-8") as rf:
   rf.write("ОТСЧЁТ ПО СКЛАДУ\n")

   rf.write("\nИтоговые остатки:\n")
   for product, s in inventory.items():
      rf.write(f"- {product}: {s["in"] - s["out"]}\n")
   
   rf.write("\nОбщее поступление:\n")
   for product, s in inventory.items():
      rf.write(f"- {product}: {s["in"]}\n")

   rf.write("\nОбщая отгрузка:\n")
   for product, s in inventory.items():
      rf.write(f"- {product}: {s["out"]}\n")

   rf.write(f"\nТовары с отрицательным остатком: {', '.join(neg_balance) if neg_balance else "Нет"}\n")
   rf.write(f"Товары без поступлений, но с отгрузкой: {', '.join(never_in) if never_in else "Нет"}\n")
   rf.write(f"Товар с максимальным поступлением: {max_in_item} ({max_in_value})\n")
   rf.write(f"Товар с максимальной отгрузкой: {max_out_item} ({max_out_value})\n")
   rf.write(f"Даты операций с яблоком: {', '.join(sorted(apple_dates))}\n")