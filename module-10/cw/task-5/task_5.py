from collections import deque


# row format: ticket_id|client|priority|operator|minutes
rows = [
    "TK-100|Alice|vip|Olga|8",
    "TK-101|Bob|regular|Nikita|12",
    "TK-102|Dina|vip|Olga|5",
    "TK-103|Egor|regular|Ira|20",
    "TK-104|Max|vip|Nikita|7",
    "TK-105|Lena|regular|Ira|9",
]

tickets = []
vip_queue = deque()
regular_queue = deque()
processed_ids = []
operator_minutes = {}

for row in rows:
    ticket_id, client, priority, operator, minutes_raw = row.split("|")
    ticket = {
        "ticket_id": ticket_id,
        "client": client,
        "priority": priority,
        "operator": operator,
        "minutes": int(minutes_raw),
    }
    tickets.append(ticket)

    # TODO 1: проверьте приоритет тикета
    # TODO 2: если priority == 'vip', добавьте ticket в vip_queue через append
    # TODO 3: иначе добавьте ticket в regular_queue через append
    # TODO 4: ничего не извлекайте на этом шаге, только распределяйте
    if priority == "vip":
        vip_queue.append(ticket)
    else:
        regular_queue.append(ticket)

print("VIP очередь:", list(vip_queue))
print("Regular очередь:", list(regular_queue))

# TODO 5: сначала обработайте vip_queue в цикле while queue
# TODO 6: на каждой итерации берите тикет через popleft()
# TODO 7: добавляйте ticket['ticket_id'] в processed_ids
# TODO 8: обновляйте operator_minutes:
#   - если оператора ещё нет в словаре, начните с 0
#   - прибавьте ticket['minutes']
# TODO 9: после VIP аналогично обработайте regular_queue
while vip_queue:
    ticket = vip_queue.popleft()

    processed_ids.append(ticket["ticket_id"])

    operator = ticket["operator"]
    minutes = ticket["minutes"]

    if operator not in operator_minutes:
        operator_minutes[operator] = 0

    operator_minutes[operator] += minutes

while regular_queue:
    ticket = regular_queue.popleft()

    processed_ids.append(ticket["ticket_id"])

    operator = ticket["operator"]
    minutes = ticket["minutes"]

    if operator not in operator_minutes:
        operator_minutes[operator] = 0

    operator_minutes[operator] += minutes

top_operator = None
top_minutes = 0

for operator, total in operator_minutes.items():
    if total > top_minutes:
        top_operator = operator
        top_minutes = total

print("Порядок обработки:", processed_ids)
print("Минуты по операторам:", operator_minutes)
print("Самый загруженный оператор:", top_operator, top_minutes)
