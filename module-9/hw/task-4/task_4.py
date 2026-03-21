# rows: ticket_id|client|title|estimate_hours|status
rows = [
    'TK-100|Acme|Ошибка в отчёте|3.5|new',
    'TK-101|Beta|Починить интеграцию|5|in_progress',
    'TK-102|Acme|Обновить доступы|2|new',
    'TK-103|Delta|Проверить выгрузку|1.5|closed',
]


class Ticket:
    allowed_statuses = {'new', 'in_progress', 'closed'}

    def __init__(self, ticket_id, client, title, estimate_hours, status):
        # TODO: сохранить ticket_id, client, title
        self.ticket_id = ticket_id
        self.client = client
        self.title = title

        # TODO: hours хранить через внутреннее поле self._estimate_hours
        # TODO: значение estimate_hours пропустить через property/setter
        self.estimate_hours = estimate_hours

        # TODO: проверить, что status входит в allowed_statuses, иначе ValueError
        if status not in self.allowed_statuses:
            raise ValueError(f"Неверный статус. {self.allowed_statuses}")
        self.status = status

    @property
    def estimate_hours(self):
        # TODO: вернуть текущее число часов
        return self._estimate_hours

    @estimate_hours.setter
    def estimate_hours(self, value):
        # TODO: привести value к float
        val = float(value)

        # TODO: если value <= 0 -> raise ValueError('Hours must be > 0')
        if val <= 0:
            raise ValueError('Часы должны быть больше 0')
        
        # TODO: сохранить результат в self._estimate_hours
        self._estimate_hours = val

    def close(self):
        # TODO: перевести задачу в статус 'closed'
        self.status = 'closed'

    def reopen(self):
        # TODO: перевести задачу обратно в статус 'new'
        self.status = 'new'

    @classmethod
    def from_row(cls, row):
        # TODO: split по '|'
        parts = row.split('|')

        # TODO: ожидать 5 частей: ticket_id, client, title, estimate_hours, status
        if len(parts) != 5:
            raise ValueError("Ожидалось 5 частей")
        
        # TODO: вернуть Ticket(...)
        return cls(parts[0], parts[1], parts[2], parts[3], parts[4])

    def __repr__(self):
        # TODO: вернуть строку вида Ticket(ticket_id='...', client='...', status='...')
        return f"Ticket(ticket_id='{self.ticket_id}', client='{self.client}', status='{self.status}')"


class TicketBoard:
    def __init__(self):
        self.tickets = []

    def add(self, ticket):
        # TODO: добавить объект Ticket в self.tickets
        self.tickets.append(ticket)

    def load(self, rows):
        # TODO: для каждой строки создать Ticket.from_row(row)
        # TODO: добавить тикет в доску через add(...)
        for row in rows:
            self.add(Ticket.from_row(row))

    def open_tickets(self):
        # TODO: вернуть список тикетов, у которых status != 'closed'
        return [t for t in self.tickets if t.status != 'closed']

    def by_client(self, client):
        # TODO: вернуть список тикетов только нужного клиента
        return [t for t in self.tickets if t.client == client]

    def total_hours_by_client(self):
        # TODO: собрать dict вида client -> total_hours
        totals = {}
        # TODO: суммировать estimate_hours по каждому клиенту
        for t in self.tickets:
            totals[t.client] = totals.get(t.client, 0.0) + t.estimate_hours
        return totals
    
    def busiest_client(self):
        # TODO: использовать total_hours_by_client()
        totals = self.total_hours_by_client()
        if not totals: return None
        # TODO: вернуть tuple (client, total_hours) с максимумом
        client = max(totals, key=totals.get)
        return (client, totals[client])


board = TicketBoard()

# TODO: загрузить строки в board
board.load(rows)

# TODO: вывести все тикеты
print("Все тикеты:", board.tickets)

# TODO: вывести только открытые тикеты
print("Открытые тикеты:", board.open_tickets())

# TODO: вывести задачи клиента 'Acme'
print("Задачи Acme:", board.by_client('Acme'))

# TODO: вывести total_hours_by_client()
print("Часы по клиентам:", board.total_hours_by_client())

# TODO: вывести busiest_client()
print("Самый загруженный:", board.busiest_client())

# TODO: закрыть первую открытую задачу и снова вывести open_tickets()
opened = board.open_tickets()
if opened:
    opened[0].close()
    print("После закрытия одной задачи:", board.open_tickets())