from collections import deque
from dataclasses import dataclass, field
from typing import Optional


catalog_paths = [
    "Каталог/Ноутбуки/Игровые",
    "Каталог/Ноутбуки/Ультрабуки",
    "Каталог/Смартфоны/Android",
    "Каталог/Смартфоны/iPhone",
    "Каталог/Аксессуары/Клавиатуры",
]

route_steps = ["A-01", "B-14", "C-07", "PACK"]

history_actions = [
    ("visit", "/catalog"),
    ("visit", "/catalog/notebooks"),
    ("visit", "/product/ultrabook-15"),
    ("back", 1),
    ("visit", "/catalog/accessories"),
    ("back", 1),
    ("forward", 1),
]

order_rows = [
    "ORD-100|Alice|Ноутбук",
    "ORD-101|Bob|Клавиатура",
    "ORD-102|Dina|Смартфон",
    "ORD-103|Alice|Мышь",
]

stocks = {
    "keyboard": 10,
    "mouse": 8,
    "monitor": 4,
}

stock_commands = [
    "remove|keyboard|2",
    "add|mouse|3",
    "undo",
    "remove|monitor|1",
    "remove|mouse|4",
    "undo",
]


@dataclass
class TreeNode:
    name: str
    children: dict[str, "TreeNode"] = field(default_factory=dict)


def add_catalog_path(root: TreeNode, path: str) -> None:
    # TODO: разбить строку пути на части через '/'
    # TODO: завести указатель current = root
    # TODO: пройти циклом по каждой части пути
    # TODO: если дочернего узла еще нет, создать его
    # TODO: сдвинуть current в найденного или созданного ребенка
    current = root
    for part in path.split('/'):
        if part not in current.children:
            current.children[part] = TreeNode(part)
        current = current.children[part]


def get_leaf_paths(root: TreeNode, prefix: str = "") -> list[str]:
    # TODO: сформировать current_path для текущего узла
    # TODO: если у узла нет детей, вернуть список из одного полного пути
    # TODO: иначе рекурсивно обойти всех детей
    # TODO: собрать и вернуть один общий список leaf-путей
    current_path = f"{prefix}/{root.name}" if prefix else root.name

    if not root.children:
        return [current_path]
    
    result = []
    for child in root.children.values():
        result.append(get_leaf_paths(child, current_path))
    return result


@dataclass
class RouteNode:
    cell: str
    next: Optional["RouteNode"] = None


def build_route(steps: list[str]) -> Optional[RouteNode]:
    # TODO: если steps пустой, вернуть None
    # TODO: создать голову списка из первого шага
    # TODO: хранить current как хвост уже построенного маршрута
    # TODO: для остальных шагов создавать новый узел и цеплять в current.next
    # TODO: после каждой вставки переносить current на новый узел
    # TODO: вернуть голову маршрута
    if not steps:
        return None
    
    head = RouteNode(steps[0])
    current = head

    for step in steps[1:]:
        current.next = RouteNode(step)
        current = current.next

    return head


def route_to_list(head: Optional[RouteNode]) -> list[str]:
    # TODO: создать пустой список result
    # TODO: пройти по односвязному списку от head до None
    # TODO: на каждом шаге добавлять cell в result
    # TODO: вернуть result
    result = []
    current = head

    while current is not None:
        result.append(current.cell)
        current = current.next

    return result


@dataclass
class HistoryNode:
    url: str
    prev: Optional["HistoryNode"] = None
    next: Optional["HistoryNode"] = None


class BrowserHistory:
    def __init__(self, homepage: str):
        # TODO: создать первый узел истории
        # TODO: сохранить его в self.current
        self.current = HistoryNode(homepage)

    def visit(self, url: str) -> None:
        # TODO: если впереди была история, оборвать self.current.next
        # TODO: создать новый узел new_node
        # TODO: связать self.current.next -> new_node
        # TODO: связать new_node.prev -> self.current
        # TODO: сделать self.current = new_node
        self.current.next = None
        new_node = HistoryNode(url, prev = self.current)
        self.current.next = new_node
        self.current = new_node

    def back(self, steps: int) -> str:
        # TODO: повторять steps раз или пока prev существует
        # TODO: двигать self.current = self.current.prev
        # TODO: вернуть url текущей страницы
        while steps > 0 and self.current.prev is not None:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def forward(self, steps: int) -> str:
        # TODO: повторять steps раз или пока next существует
        # TODO: двигать self.current = self.current.next
        # TODO: вернуть url текущей страницы
        while steps > 0 and self.current.prev is not None:
            self.current = self.current.prev
            steps -= 1
        return self.current.url

    def get_current_url(self) -> str:
        # TODO: просто вернуть self.current.url
        return self.current.url

    def get_full_history(self) -> list[str]:
        # TODO: от текущего узла дойти назад до самого первого
        # TODO: затем пройти вперед и собрать все url в список
        # TODO: вернуть список полной истории
        current_node = self.current
        while current_node.prev is not None:
            current_node = current_node.prev

        urls = []
        current = current_node
        while current is not None:
            urls.append(current.url)
            current = current.next

        return urls


catalog_root = TreeNode("Магазин")
for path in catalog_paths:
    # TODO: добавить каждый путь в дерево каталога
    add_catalog_path(catalog_root, path)

route_head = build_route(route_steps)

history = BrowserHistory("/home")
history_results = []
for action, value in history_actions:
    # TODO: для visit просто открыть новую страницу
    # TODO: для back и forward сохранить результат перехода в history_results
    if action == "visit":
        history.visit(value)
    elif action == "back":
        history_results.append(("back", history.back(value)))
    elif action == "forward":
        history_results.append(("forward", history.forward(value)))


order_queue = deque()
processed_orders = []

for row in order_rows:
    # TODO: разобрать строку заказа на поля
    # TODO: собрать словарь order
    # TODO: положить order в хвост очереди через append
    order_id, client, product = row.split("|")
    order = {
        "order_id": order_id,
        "client": client,
        "product": product,
    }
    order_queue.append(order)


while order_queue:
    # TODO: достать заказ из начала очереди через popleft
    # TODO: добавить его id в processed_orders
    # TODO: в этом месте можно было бы запускать сборку заказа
    order = order_queue.popleft()
    processed_orders.append(order["order_id"])


history_stack = []
undo_count = 0
errors = []

for command in stock_commands:
    if command == "undo":
        # TODO: если стек не пуст, взять верхний снимок через pop
        # TODO: присвоить stocks восстановленное состояние
        # TODO: увеличить undo_count
        if history_stack:
            stocks = history_stack.pop()
            undo_count += 1
        continue

    # TODO: разобрать команду на action, sku, qty
    action, sku, qty_raw = command.split("|")
    qty = int(qty_raw)

    if action == "add":
        # TODO: сохранить копию stocks в history_stack
        # TODO: увеличить остаток по sku
        history_stack.append(stocks.copy())
        stocks[sku] = stocks.get(sku, 0) + qty

    elif action == "remove":
        # TODO: если товара недостаточно, записать текст ошибки
        # TODO: иначе сохранить снимок в стек
        # TODO: после этого уменьшить остаток по sku
        if stocks.get(sku, 0) < qty:
            errors.append(f"Недостаточное кол-во товара")
            continue

        history_stack.append(stocks.copy())
        stocks[sku] -= qty


print("Конечные пути каталога:")
for path in get_leaf_paths(catalog_root):
    print(path)

print("Маршрут сборки:", route_to_list(route_head))
print("Результаты back/forward:", history_results)
print("Текущая страница:", history.get_current_url())
print("Полная история:", history.get_full_history())
print("Порядок обработки заказов:", processed_orders)
print("Ошибки склада:", errors)
print("Успешных undo:", undo_count)
print("Финальные остатки:", stocks)
