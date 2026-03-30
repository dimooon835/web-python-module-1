subscriptions = {
    "Alice": {"music", "video"},
    "Bob": {"music"},
    "Dina": set(),
}

commands = [
    "add|Dina|books",
    "remove|Alice|video",
    "remove|Bob|cloud",
    "report",
    "undo",
    "add|Bob|cloud",
    "undo",
    "undo",
    "report",
]

history_stack = []
reports = []
errors = []
undo_count = 0

def copy(subs):
    return {user: set(services) for user, services in subs.items()}

for command in commands:
    if command == "undo":
        # TODO 1: проверьте, что history_stack не пуст
        # TODO 2: если есть состояние, достаньте его через pop()
        # TODO 3: присвойте subscriptions извлечённое состояние
        # TODO 4: увеличьте undo_count на 1
        # TODO 5: если стек пуст, просто пропустите команду
        if history_stack:
            subscriptions = history_stack.pop()
            undo_count += 1
        else:
            pass
        continue

    if command == "report":
        # TODO 6: сделайте независимую копию subscriptions
        #   подсказка: у каждого пользователя нужно копировать set отдельно
        # TODO 7: добавьте копию в reports
        reports.append(copy(subscriptions))
        continue

    action, user, service = command.split("|")
    current_services = subscriptions.get(user, set())

    if action == "add":
        # TODO 8: перед изменением сохраните снимок subscriptions в history_stack
        # TODO 9: если user отсутствует, создайте для него пустой set
        # TODO 10: добавьте service в subscriptions[user]
        history_stack.append(copy(subscriptions))

        if user not in subscriptions:
            subscriptions[user] = set()

        subscriptions[user].add(service)

    elif action == "remove":
        # TODO 11: если service отсутствует у пользователя,
        #   добавьте текст ошибки в errors и не меняйте состояние
        # TODO 12: если service есть,
        #   сначала сохраните снимок subscriptions в history_stack,
        #   затем удалите service из subscriptions[user]
        if service not in current_services:
            errors.append(f"{user} не подписан на {service}")
        else:
            history_stack.append(copy(subscriptions))
            subscriptions[user].remove(service)


print("Отчёты:", reports)
print("Ошибки:", errors)
print("Успешных undo:", undo_count)
print("Финальные подписки:", subscriptions)
