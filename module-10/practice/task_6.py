from collections import deque
from copy import deepcopy


# row format: order_id|client|priority|category_path|items
rows = [
    "ORD-900|Alice|express|electronics/phones|2",
    "ORD-901|Bob|normal|home/kitchen|4",
    "ORD-902|Dina|express|electronics/laptops|1",
    "ORD-903|Max|normal|home/decor|3",
    "ORD-904|Olga|normal|sports/running|2",
    "ORD-905|Ira|express|sports/cycling|1",
]

# command format:
# - pull_next
# - pack|operator|minutes
# - undo
# - report
commands = [
    "pull_next",
    "pack|Nikita|12",
    "pull_next",
    "pack|Olga|9",
    "pull_next",
    "report",
    "pack|Nikita|8",
    "undo",
    "pull_next",
    "pack|Ira|11",
    "pull_next",
    "pack|Olga|7",
    "report",
]

category_tree = {
    "name": "root",
    "count": 0,
    "children": {
        "electronics": {
            "name": "electronics",
            "count": 0,
            "children": {
                "phones": {"name": "phones", "count": 0, "children": {}},
                "laptops": {"name": "laptops", "count": 0, "children": {}},
            },
        },
        "home": {
            "name": "home",
            "count": 0,
            "children": {
                "kitchen": {"name": "kitchen", "count": 0, "children": {}},
                "decor": {"name": "decor", "count": 0, "children": {}},
            },
        },
        "sports": {
            "name": "sports",
            "count": 0,
            "children": {
                "running": {"name": "running", "count": 0, "children": {}},
                "cycling": {"name": "cycling", "count": 0, "children": {}},
            },
        },
    },
}

orders = []
express_queue = deque()
normal_queue = deque()

current_order = None
packed_orders = []
operator_minutes = {}
history_stack = []
reports = []
errors = []
undo_count = 0


def build_order(row):
    order_id, client, priority, category_path_raw, items_raw = row.split("|")
    return {
        "order_id": order_id,
        "client": client,
        "priority": priority,
        "category_path": category_path_raw.split("/"),
        "items": int(items_raw),
    }


def push_snapshot():
    snapshot = {
        "current_order": deepcopy(current_order),
        "packed_orders": deepcopy(packed_orders),
        "operator_minutes": deepcopy(operator_minutes),
        "category_tree": deepcopy(category_tree),
    }
    history_stack.append(snapshot)


def restore_snapshot(snapshot):
    global current_order, packed_orders, operator_minutes, category_tree
    current_order = snapshot["current_order"]
    packed_orders = snapshot["packed_orders"]
    operator_minutes = snapshot["operator_minutes"]
    category_tree = snapshot["category_tree"]


def update_category_counts(path_parts):
    node = category_tree

    # TODO 1: увеличьте node['count'] у корня перед проходом по path_parts
    # TODO 2: для каждого part из path_parts:
    #   - проверьте, что part есть в node['children']
    #   - если нет, верните False
    #   - если есть, перейдите к дочернему узлу
    #   - увеличьте у него поле 'count' на 1
    # TODO 3: если весь путь успешно пройден, верните True
    node["count"] += 1

    for part in path_parts:
        if part not in node["children"]:
            return False
        node = node["children"][part]
        node["count"] += 1

    return True

def pull_next_order():
    # TODO 4: если express_queue не пуст, вернуть express_queue.popleft()
    # TODO 5: иначе если normal_queue не пуст, вернуть normal_queue.popleft()
    # TODO 6: если обе очереди пусты, вернуть None
    if express_queue:
        return express_queue.popleft()
    
    if normal_queue:
        return normal_queue.popleft()
    
    return None

for row in rows:
    order = build_order(row)
    orders.append(order)

    # TODO 7: разложите orders по двум очередям:
    #   - priority == 'express' -> express_queue.append(order)
    #   - иначе -> normal_queue.append(order)
    for order in orders:
        if order["priority"] == "express":
            express_queue.append(order)
        else:
            normal_queue.append(order)

for command in commands:
    if command == "pull_next":
        # TODO 8: если current_order уже есть,
        #   добавьте ошибку о том, что заказ уже взят в работу, и continue
        # TODO 9: получите следующий заказ через pull_next_order()
        # TODO 10: если заказ найден, положите его в current_order
        # TODO 11: если заказа нет, добавьте ошибку "Очереди пусты"
        if current_order is not None:
            errors.append("Заказ уже в работе")
            continue

        order = pull_next_order()

        if order:
            current_order = order
        else:
            errors.append("Очереди пусты")

    if command == "undo":
        # TODO 12: если history_stack не пуст,
        #   достаньте последний snapshot через pop,
        #   восстановите состояние через restore_snapshot,
        #   увеличьте undo_count
        # TODO 13: если стек пуст, добавьте ошибку "Нечего откатывать"
        if history_stack:
            snapshot = history_stack.pop()
            restore_snapshot(snapshot)
            undo_count += 1
        else:
            errors.append("Нечего откатывать")

    if command == "report":
        # TODO 14: найдите самого загруженного оператора:
        #   - top_operator (имя или None)
        #   - top_minutes (число минут)
        # TODO 15: добавьте в reports словарь со срезом состояния:
        #   {
        #     'current_order': current_order['order_id'] или None,
        #     'express_left': len(express_queue),
        #     'normal_left': len(normal_queue),
        #     'packed_total': len(packed_orders),
        #     'top_operator': top_operator,
        #     'top_minutes': top_minutes,
        #   }
        if operator_minutes:
            top_operator = max(operator_minutes, key=operator_minutes.get)
            top_minutes = operator_minutes[top_operator]
        else:
            top_operator = None
            top_minutes = 0

        reports.append({
            'current_order': current_order['order_id'] if current_order else None,
            'express_left': len(express_queue),
            'normal_left': len(normal_queue),
            'packed_total': len(packed_orders),
            'top_operator': top_operator,
            'top_minutes': top_minutes,
        })

    if command.startswith("pack|"):
        _, operator, minutes_raw = command.split("|")
        minutes = int(minutes_raw)

        # TODO 16: если current_order is None,
        #   добавьте ошибку "Нет заказа в работе" и continue
        # TODO 17: перед любыми изменениями вызовите push_snapshot()
        # TODO 18: обновите operator_minutes для operator,
        #   прибавив minutes (с инициализацией 0 при первом вхождении)
        # TODO 19: добавьте запись в packed_orders:
        #   {
        #     'order_id': current_order['order_id'],
        #     'client': current_order['client'],
        #     'operator': operator,
        #     'minutes': minutes,
        #     'items': current_order['items'],
        #     'category_path': '/'.join(current_order['category_path']),
        #   }
        # TODO 20: обновите category_tree через update_category_counts(current_order['category_path'])
        # TODO 21: если update_category_counts вернул False,
        #   добавьте ошибку с order_id и сделайте откат через restore_snapshot(history_stack.pop())
        # TODO 22: если обновление успешно, очистите current_order = None
        if current_order is None:
            errors.append("Нет заказа в работе")
            continue

        push_snapshot()

        operator_minutes[operator] = operator_minutes.get(operator, 0) + minutes

        packed_orders.append({
            'order_id': current_order['order_id'],
            'client': current_order['client'],
            'operator': operator,
            'minutes': minutes,
            'items': current_order['items'],
            'category_path': '/'.join(current_order['category_path']),
        })

        success = update_category_counts(current_order["category_path"])

        if not success:
            errors.append("Ошибка категории у заказа")
            snapshot = history_stack.pop()
            restore_snapshot(snapshot)
        else:
            current_order = None

    errors.append(f"Неизвестная команда: {command}")

print("Итог упакованных заказов:", packed_orders)
print("Минуты по операторам:", operator_minutes)
print("Отчёты смены:", reports)
print("Ошибки:", errors)
print("Успешных undo:", undo_count)
print("Категории (root count):", category_tree["count"])
