# import random
# tasks = []

# for i in range(10):
#     tasks.append({
#         "id": f"t {i}",
#         "assignee": random.choice(["ivan", "olga", "petr", "anna", "oleg"]),
#         "status": random.choice(["in progress", "blocked", "in review", "waiting vendor"]),
#         "days in status": random.randint(0, 10)
#     })

# def find_in_progress(tasks):
#     result = {}
#     for task in tasks:
#         if task["status"] == "in progress" and task["days in status"] > 7:
#             if task["assignee"] in result:
#                 result[task["assignee"]] += task["days in status"]
#             else:
#                 result[task["assignee"]] = task["days in status"]
#     return result

# def find_unique_status(tasks):
#     result2 = {}
#     for task in tasks:
#         if task["status"] in result2:
#             result2[task["status"]] += 1
#         else:
#             result2[task["status"]] = 1
#     return result2

# def find_debt(tasks):
#     result3 = {}
#     for task in tasks:
#         if task["status"] in ["in progress", "blocked"]:
#             if task["assignee"] in result3:
#                 result3[task["assignee"]] += task["days in status"]
#             else:
#                 result3[task["assignee"]] = task["days in status"]
#     return result3

# progress = find_in_progress(tasks)
# status = find_unique_status(tasks)
# debt = find_debt(tasks)
# max_debt_assignee = max(debt, key = debt.get)
# max_debt = debt[max_debt_assignee]

# for assignee, days in progress.items():
#     print(f"Исполнитель: {assignee}: {days} дней")

# for status, assignee in status.items():
#     print(f"Статус: {status}: {assignee}")

# print(f"Исполнитель: {max_debt_assignee}, Долг: {max_debt} дней")


# logs = [
#     ("ivan", "day", 8),
#     ("ivan", "night", 4),
#     ("olga", "day", 6),
#     ("petr", "night", 7),
#     ("anna", "day", 4),
#     ("anna", "day", 3)
# ]

# employee_shifts = {}
# shift_hours = {}
# employee_hours = {}

# for name, shift, hours in logs:
#     if name not in employee_shifts:
#         employee_shifts[name] = set()
#     employee_shifts[name].add(shift)

#     if shift not in shift_hours:
#         shift_hours[shift] = 0
#     shift_hours[shift] += hours

#     if shift not in employee_hours:
#         employee_hours[name] = 0
#     employee_hours[name] += hours

# # employees_shifts = [name for name, shifts in employee_shifts.items() if len(shifts) > 1]
# # shifts_8h = [shift for shift, total in shift_8h.items() if total < 8]
# # employees_12h = [name for name, total in employee_12h.items() if total >= 12]

# multiple_shift = []
# for employee in employee_shifts:
#     if len(employee_shifts[employee]) == 2:
#         multiple_shift.append(employee)

# shifts_less = {}
# for shift in shift_hours:
#     if shift_hours[shift] < 8:
#         shifts_less.append(shift)

# employees = []
# for employee in employee_hours:
#     if employee_hours[employee] >= 12:
#         employees.append(employee)

# print(multiple_shift)
# print(shifts_less)
# print(employees)


history = [
    ("t_1", "new"), ("t_1", "in progress"), ("t_1", "done"),
    ("t_2", "new"), ("t_2", "done"),
    ("t_3", "new"), ("t_3", "in progress"), ("t_3", "cancelled"),
    ("t_4", "new"), ("t_4", "cancelled"), ("t_4", "done")
]

allowed = {
    ("new", "in progress"),
    ("new", "cancleed"),
    ("in progress", "done"),
    ("in progress", "cancelled")
}

# from collections import defaultdict
# entities = defaultdict(list)
# for obj, status in history:
#     entities[obj].append(status)

# not_entities = []
# for obj, statuses in entities.items():
#     for i in range(len(statuses) - 1):
#         transition = (statuses[i], statuses[i + 1])
#         if transition not in allowed:
#             not_entities.append(obj)
#             break

# print(not_entities)

last_status = {}
errors = {}
for entity, status in history:
    if entity not in last_status:
        last_status[entity] = status
        continue

    prev = last_status[entity]
    if (prev, status) not in allowed:
        if entity not in errors:
            errors[entity] = (prev, status)
        else:
            last_status[entity] = status

for entity, transition in errors.items():
    print(entity, ":", transition)