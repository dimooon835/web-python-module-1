from dataclasses import dataclass
from typing import Optional, Dict, List, Tuple


stocks = {
    'MSK-1': {'keyboard': 10, 'mouse': 20, 'monitor': 4},
    'SPB-2': {'keyboard': 6, 'dock': 5, 'monitor': 2},
    'KZN-3': {'mouse': 7, 'dock': 3, 'laptop': 2},
}

# rows: request_id|client|warehouse_id|sku|quantity
rows = [
    'RQ-100|Acme|MSK-1|keyboard|3',
    'RQ-101|Beta|SPB-2|dock|2',
    'RQ-102|Acme|MSK-1|monitor|5',
    'RQ-103|Delta|X-999|mouse|1',
    'RQ-104|Gamma|KZN-3|laptop|0',
    'RQ-105|Beta|SPB-2|chair|1',
    'RQ-101|Beta|MSK-1|mouse|4',
    'RQ-106|Acme|MSK-1|mouse|7',
    'RQ-107|Kira|KZN-3|laptop|1',
]


class ReservationError(Exception):
    pass


class RowFormatError(ReservationError):
    pass


class WarehouseNotFoundError(ReservationError):
    pass


class ProductNotFoundError(ReservationError):
    pass


class QuantityError(ReservationError):
    pass


class StockLimitError(ReservationError):
    pass


class DuplicateRequestError(ReservationError):
    pass


@dataclass(order=True)
class ReservationRequest:
    request_id: str
    client: str
    warehouse_id: str
    sku: str
    quantity: int


class Warehouse:
    def __init__(self, warehouse_id: str, products: Dict[str, int]):
        # TODO: сохранить warehouse_id
        self.warehouse_id = warehouse_id

        # TODO: создать отдельную копию словаря products
        self.products = products.copy()
        
        # TODO: создать список reservations
        self.reservations = List[ReservationRequest] = []
        pass

    def has_sku(self, sku: str) -> bool:
        # TODO: вернуть True/False, есть ли такой sku в self.products
        return sku in self.products

    def available(self, sku: str) -> int:
        # TODO: вернуть текущий остаток по sku
        return self.products.get(sku, 0)

    def reserve(self, request: ReservationRequest):
        # TODO: если request.sku отсутствует -> raise ProductNotFoundError(...)
        if not self.has_sku(request.sku):
            raise ProductNotFoundError(f"Продукт '{request.sku}' не найден в {self.warehouse_id}")
        
        # TODO: если request.quantity > available(...) -> raise StockLimitError(...)
        if request.quantity > self.available(request.sku):
            raise StockLimitError(f"Недостаточно места для '{request.sku}' (требуется {request.quantity}, доступно {self.available(request.sku)})")
        
        # TODO: уменьшить остаток на складе
        self.products[request.sku] -= request.quantity

        # TODO: добавить request в self.reservations
        self.reservations.append(request)

    def total_left(self) -> int:
        # TODO: вернуть сумму всех остатков на складе
        return sum(self.products.values())

    def reserved_total(self) -> int:
        # TODO: вернуть сумму quantity по всем self.reservations
        return sum(r.quantity for r in self.reservations)


class ReservationService:
    def __init__(self, stocks: Dict[str, Dict[str, int]]):
        # TODO: создать warehouses вида warehouse_id -> Warehouse(...)
        self.warehouse = {wid: Warehouse(wid, items) for wid, items in stocks.items()}

        # TODO: создать списки accepted и errors
        self.accepted = List[ReservationRequest] = []
        self.errors = List[Tuple[str, str, str]] = []

        # TODO: создать множество processed_ids
        self.processed_ids = set()

    def parse_request(self, row: str):
        # TODO: split по '|'
        parts = row.split('|')

        # TODO: ожидать 5 частей: request_id, client, warehouse_id, sku, quantity_raw
        if len(parts) != 5:
            raise RowFormatError(f"Неправильный формат: ожидалось 5 частей")
        
        # TODO: quantity_raw преобразовать в int
        req_id, client, w_id, sku, qty_raw = parts
        try:
            qty = int(qty_raw)
        except ValueError:
            raise QuantityError(f"Неправильное кол-во: {qty_raw}")
        
        # TODO: если warehouse_id не существует -> WarehouseNotFoundError
        if w_id not in self.warehouse:
            raise WarehouseNotFoundError(f"Warehouse '{w_id}' не существует")

        # TODO: если quantity <= 0 -> QuantityError
        if qty <= 0:
            raise QuantityError(f"Кол-во должно быть больше нуля")
        
        # TODO: вернуть объект ReservationRequest(...)
        return ReservationRequest(req_id, client, w_id, sku, qty)

    def submit(self, row: str):
        # TODO: внутри try вызвать parse_request(row)
        try:
            request = self.parse_request(row)

        # TODO: если request.request_id уже в processed_ids -> DuplicateRequestError
            if request.request_id in self.processed_ids:
                raise DuplicateRequestError(f"Requset ID '{request.request_id}' уже обработан")
        
        # TODO: затем warehouses[request.warehouse_id].reserve(request)
            self.warehouses[request.warehouse_id].reserve(request)

        # TODO: после успеха добавить request_id в processed_ids
            self.processed_ids.add(request.request_id)

        # TODO: добавить request в self.accepted
            self.accepted.append(request)

        # TODO: ReservationError сохранить в self.errors как (row, error_type, message)
        except ReservationError as e:
            self.errors.append((row, e.__class__.__name__, str(e)))

    def load(self, rows: List[str]):
        # TODO: вызвать submit(row) для каждой строки
        for row in rows:
            self.submit(row)

    def client_totals(self) -> Dict[str, int]:
        # TODO: собрать dict вида client -> total_reserved_quantity
        totals = {}
        for req in self.accepted:
            totals[req.client] = totals.get(req.client, 0) + req.quantity
        return totals

    def top_client(self) -> Optional[Tuple[str, int]]:
        # TODO: использовать client_totals()
        totals = self.client_totals()
        if not totals:
            return None
    
        # TODO: вернуть tuple(client, total_quantity) с максимумом
        return max(totals.items(), key = lambda x: x[1])

    def lowest_stock_warehouse(self) -> Tuple[str, int]:
        # TODO: найти склад с минимумом total_left()
        # TODO: вернуть tuple(warehouse_id, total_left)
        return min([(w.warehouse_id, w.total_left()) for w in self.warehouses.values()], key = lambda x: x[1])

    def warehouse_snapshot(self) -> Dict[str, Dict[str, int]]:
        # TODO: собрать dict вида warehouse_id -> копия текущих остатков products
        return {wid: w.products.copy() for wid, w in self.warehouses.items()}

    def find_request(self, request_id) -> Optional[ReservationRequest]:
        # TODO: вернуть Optional[ReservationRequest]
        # TODO: пройтись по self.accepted и найти нужную заявку
        # TODO: если не найдено -> вернуть None
        return next((r for r in self.accepted if r.request_id == request_id), None)


service = ReservationService(stocks)

# TODO: загрузить rows через service.load(rows)
service.load(rows)

# TODO: вывести принятые заявки
print("Принятые заявки: ", [r.request_id for r in service.accepted])

# TODO: вывести ошибки
print("\nЖурнал ошибок:")
for err in service.errors:
    print(f"Row: {err[0]} | Type: {err[1]} | Msg: {err[2]}")

# TODO: вывести warehouse_snapshot()
print("\nСнимок складов:", service.warehouse_snapshot())

# TODO: вывести client_totals()
print("\nИтоги по клиентам", service.client_totals())

# TODO: вывести top_client()
print("\nТоп клиент", service.top_client())

# TODO: вывести lowest_stock_warehouse()
print("\nСклад с мин. остатком", service.lowest_stock_warehouse())

# TODO: вывести find_request('RQ-107')
print("\nПоиск RQ-107", service.find_request('RQ-107'))