import random
tasks = []

for i in range(10):
    tasks.append({
        "id": f"t {i}",
        "assignee": random.choice(["ivan", "olga", "petr", "anna", "oleg"]),
        "status": random.choice(["in progress", "blocked", "in review", "waiting vendor"]),
        "days in status": random.randint(0, 10)
    })

def find_in_progress(tasks):
    result = {}
    for task in tasks:
        if task["status"] == "in progress" and task["days in status"] > 7:
            if task["assignee"] in result:
                result[task["assignee"]] += task["days in status"]
            else:
                result[task["assignee"]] = task["days in status"]
    return result

def find_unique_status(tasks):
    result2 = {}
    for task in tasks:
        if task["status"] in result2:
            result2[task["status"]] += 1
        else:
            result2[task["status"]] = 1
    return result2

def find_debt(tasks):
    result3 = {}
    for task in tasks:
        if task["status"] in ["in progress", "blocked"]:
            if task["assignee"] in result3:
                result3[task["assignee"]] += task["days in status"]
            else:
                result3[task["assignee"]] = task["days in status"]
    return result3

progress = find_in_progress(tasks)
status = find_unique_status(tasks)
debt = find_debt(tasks)
max_debt_assignee = max(debt, key = debt.get)
max_debt = debt[max_debt_assignee]

for assignee, days in progress.items():
    print(f"Исполнитель: {assignee}: {days} дней")

for status, assignee in status.items():
    print(f"Статус: {status}: {assignee}")

print(f"Исполнитель: {max_debt_assignee}, Долг: {max_debt} дней")