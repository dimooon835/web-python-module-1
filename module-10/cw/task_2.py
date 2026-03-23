commands = [
    "append:Привет",
    "append:, мир",
    "show",
    "append:!",
    "show",
    "undo",
    "show",
    "append:!!!",
    "undo",
    "undo",
    "undo",
    "show",
]


text = ""
state_stack = []
snapshots = []
undo_count = 0
max_stack_size = 0

for command in commands:
    if command.startswith("append:"):
        value = command.split(":", 1)[1]
        # TODO: сохранить текущее состояние текста в стек
        # TODO: обновить max_stack_size
        # TODO: добавить value к text
        state_stack.append(text)

        if len(state_stack) > max_stack_size:
            max_stack_size = len(state_stack)

        text += value

    elif command == "undo":
        # TODO: если стек не пуст, достать последнее состояние
        # TODO: увеличить undo_count
        if state_stack:
            text = state_stack.pop()
            undo_count += 1

    elif command == "show":
        # TODO: добавить текущее состояние текста в snapshots
        snapshots.append(text)

print("Снимки:", snapshots)
print("Финальный текст:", text)
print("Количество undo:", undo_count)
print("Максимальная глубина стека:", max_stack_size)
