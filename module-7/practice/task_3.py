"""
ЗАДАЧА: Умный контроль доступа (бейджи)

Даны записи содержащие журнал проходов сотрудников.

Каждая строка файла имеет формат:
дата,имя,действие

Где:
- дата     — строка в формате YYYY-MM-DD
- имя      — имя человека
- действие — ENTER (вход) или EXIT (выход)

Журнал проходов:
2026-02-01,Иван,ENTER
2026-02-01,Мария,ENTER
2026-02-01,Иван,EXIT
2026-02-01,Иван,EXIT
2026-02-01,Олег,EXIT
2026-02-02,Мария,EXIT
2026-02-02,Олег,ENTER

НЕОБХОДИМО РЕАЛИЗОВАТЬ:

1. Записать проходы в файл access.log

2. Прочитать файл access.log и загрузить данные.

3. Для каждого человека:
   - посчитать количество входов (ENTER)
   - посчитать количество выходов (EXIT)
   - определить, находится ли человек ВНУТРИ в конце лога
     (ENTER без последующего EXIT)

4. Найти людей с ошибками доступа:
   - EXIT без предварительного ENTER
   - два ENTER подряд без EXIT
   (сохранить таких людей в множество)

5. Для каждой даты посчитать количество входов (ENTER).

6. Найти дату с максимальным количеством входов.

7. Записать подробный отчёт в файл access_report.txt.
"""


journal = [
   "2026-02-01,Иван,ENTER",
   "2026-02-01,Мария,ENTER",
   "2026-02-01,Иван,EXIT",
   "2026-02-01,Иван,EXIT",
   "2026-02-01,Олег,EXIT",
   "2026-02-02,Мария,EXIT",
   "2026-02-02,Олег,ENTER"
]

employee_data = {}
daily_enter = {}
problem_employee = set()

with open("access.log", "w", encoding = "utf-8") as f:
   f.write("\n".join(journal))

records = []

with open("access.log", "r", encoding = "utf-8") as f:
   for line in f:
      if line.strip():
         date, name, action = [x.strip() for x in line.split(",")]
         records.append({
            "date": date,
            "name": name,
            "action": action
            })

stats = {}
current_state = {}
errors = set()
daily_enter = {}

for rec in records:
      name = rec["name"]
      action = rec["action"]
      date = rec["date"]

      if name not in stats:
         stats[name] = {
            "enter": 0,
            "exit": 0,
         }
      current_state[name] = "OUTSIDE"

      if action == "ENTER":
         if current_state[name] == "INSIDE":
            errors.add(name)

         stats[name]["enter"] += 1
         current_state[name] = "INSIDE"
         daily_enter[date] = daily_enter.get(date , 0) + 1

      # if action == "EXIT":
      #    if current_state[name] == "OUTSIDE":
      #       errors.add(name)
      #    current_state[name] = "OUTSIDE"

      elif action == "EXIT":
         if current_state[name] == "OUTSIDE":
            errors.add(name)

         stats[name]["exit"] += 1
         current_state[name] == "OUTSIDE"

max_enters_count = max(daily_enter.values()) if daily_enter else 0
max_enters_date = [d for d, v in daily_enter.items() if v == max_enters_count]

with open("access_report.txt", "w", encoding = "utf-8") as rf:
   rf.write("Отчёт системы контроля доступа\n")

   rf.write(f"\n{"Имя":<10} | {"Входы":<7} | {"Выходы":<7} | {"Финальный статус":<12}\n")
   for name in stats:
      status = "Внутри" if current_state[name] == "INSIDE" else "Вышел"
      rf.write(f"{name:<10} | {stats[name]["enter"]:<7} | {stats[name]["exit"]:<7} | {status:<12}\n")

   rf.write(f"\nЛюди с ошибками доступа: {', '.join(sorted(errors)) if errors else "нет"}\n")

   rf.write("\nСтатистика по датам:\n")
   for date, count in sorted(daily_enter.items()):
      rf.write(f"- {date}: {count}\n")

   rf.write(f"\nДата с пиковой нагрзукой: {', '.join(max_enters_date)} ({max_enters_count} входов)")