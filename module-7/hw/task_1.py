lines = [
    "Понедельник,09:00,Группа1,Математика,101",
    "Понедельник,09:00,Группа2,Физика,101",
    "Понедельник,10:30,Группа1,Физика,102",
    "Понедельник,12:00,Группа3,История,103",
    "Вторник,09:00,Группа1,Информатика,101",
    "Вторник,09:00,Группа2,Математика,102",
    "Вторник,10:30,Группа3,Физика,101",
    "Вторник,12:00,Группа1,История,103",
    "Среда,09:00,Группа2,Информатика,101",
    "Среда,10:30,Группа3,Математика,101",
    "Среда,10:30,Группа1,Физика,101"
]

schedule = []  
# список всех занятий
# каждый элемент может быть словарём с ключами:
# "day", "time", "group", "subject", "room"

group_subjects = {}
# group -> список предметов этой группы

group_lesson_count = {}
# group -> общее количество занятий

room_usage = {}
# (day, time, room) -> список групп
# используется для поиска конфликтов

day_lesson_count = {}
# day -> количество занятий в этот день

conflicts = []
# список найденных конфликтов расписания


with open("schedule.txt", "w", encoding="utf-8") as file:
    # TODO: записать строки в файл
    for line in lines:
        file.write(line + "\n")


with open("schedule.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        # TODO:
        # разобрать строку
        # создать словарь занятия
        # добавить его в schedule
        parts = line.split(',')
        lesson = {
            "day": parts[0],
            "time": parts[1],
            "group": parts[2],
            "subject": parts[3],
            "room": parts[4]
        }
        schedule.append(lesson)


for lesson in schedule:
    # получить значения:
    # day, time, group, subject, room
    day, time, group, subject, room = lesson.values()

    # TODO:
    # 1) обновить group_subjects
    # 2) обновить group_lesson_count
    # 3) обновить day_lesson_count
    # 4) обновить room_usage
    if group not in group_subjects:
        group_subjects[group] = set()
    group_subjects[group].add(subject)

    group_lesson_count[group] = group_lesson_count.get(group, 0) + 1

    day_lesson_count[day] = day_lesson_count.get(day, 0) + 1

    room_key = (day, time, room)
    if room_key not in room_usage:
        room_usage[room_key] = []
    room_usage[room_key].append(group)


for (day, time, room), groups in room_usage.items():
    # key = (day, time, room)
    # groups = список групп

    # TODO:
    # если групп больше одной — это конфликт
    # сохранить информацию в conflicts
    if len(groups) > 1:
        conflicts.append({
            "day": day,
            "time": time,
            "room": room,
            "groups": groups
        })

busiest_day = None
max_lessons = 0

# TODO:
# пройтись по day_lesson_count
# найти день с максимальным количеством занятий
for day, count in day_lesson_count.items():
    if count > max_lessons:
        max_lessons = count
        busiest_day = day

with open("schedule_report.txt", "w", encoding="utf-8") as file:
    # TODO:
    # записать:
    # - статистику по группам
    # - список конфликтов
    # - самый загруженный день
    file.write("=== СТАТИСТИКА ПО ГРУППАМ ===\n")
    for group in sorted(group_lesson_count.keys()):
        subjects = ", ".join(group_subjects[group])
        count = group_lesson_count[group]
        file.write(f"{group}: Занятий: {count}, Предметы: {subjects}\n")

    file.write("\n=== КОНФЛИКТЫ АУДИТОРИЙ ===\n")
    if not conflicts:
        file.write("Конфликтов не обнаружено.\n")
    else:
        for c in conflicts:
            file.write(f"День: {c['day']}, Время: {c['time']}, Аудитория: {c['room']}. Группы: {', '.join(c['groups'])}\n")

    file.write("\n=== МАКСИМАЛЬНАЯ НАГРУЗКА ===\n")
    file.write(f"День с наибольшим количеством занятий: {busiest_day} ({max_lessons} занятий)\n")

print("Отчет сформирован в файл schedule_report.txt")