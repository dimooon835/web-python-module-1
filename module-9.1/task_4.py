from dataclasses import dataclass
from typing import Optional, Dict, List


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
    def __init__(self, warehouse_id, products: Dict[str, int]):
        # TODO: сохранить warehouse_id
        self.warehouse_id = warehouse_id

        # TODO: создать отдельную копию словаря products
        self.products = dict(products)
        
        # TODO: создать список reservations
        self.reservations: List[ReservationRequest] = []
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
        self.warehouses: Dict[str, Warehouse] = {wid: Warehouse(wid, products) for wid, products in stocks.items()}

        # TODO: создать списки accepted и errors
        self.accepted: List[ReservationRequest] = []
        self.errors: List[tuple] = []

        # TODO: создать множество processed_ids
        self.processed_ids = set()

    def parse_request(self, row: str) -> ReservationRequest:
        # TODO: split по '|'
        parts = row.split('|')

        # TODO: ожидать 5 частей: request_id, client, warehouse_id, sku, quantity_raw
        if len(parts) != 5:
            raise RowFormatError(f"Неправильный формат: ожидалось 5 частей")
        
        # TODO: quantity_raw преобразовать в int
        request_id, client, warehouse_id, sku, quantity_raw = parts
        try:
            quantity = int(quantity_raw)
        except:
            raise RowFormatError(f"Неправильное кол-во: {quantity_raw}")
        
        # TODO: если warehouse_id не существует -> WarehouseNotFoundError
        if warehouse_id not in self.warehouses:
            raise WarehouseNotFoundError(f"Warehouse '{warehouse_id}' не существует")

        # TODO: если quantity <= 0 -> QuantityError
        if quantity <= 0:
            raise QuantityError(f"Кол-во должно быть больше нуля")
        
        # TODO: вернуть объект ReservationRequest(...)
        return ReservationRequest(request_id, client, warehouse_id, sku, quantity)

    def submit(self, row: str):
        # TODO: внутри try вызвать parse_request(row)
        try:
            request = self.parse_request(row)

        # TODO: если request.request_id уже в processed_ids -> DuplicateRequestError
            if request.request_id in self.processed_ids:
                raise DuplicateRequestError(f"Requset ID '{request.request_id}' уже обработан")
        
        # TODO: затем warehouses[request.warehouse_id].reserve(request)
            warehouse = self.warehouses[request.warehouse_id]
            warehouse.reserve(request)

        # TODO: после успеха добавить request_id в processed_ids
            self.processed_ids.add(request.request_id)

        # TODO: добавить request в self.accepted
            self.accepted.append(request)

        # TODO: ReservationError сохранить в self.errors как (row, error_type, message)
        except ReservationError as e:
            self.errors.append((row, type(e).__name__, str(e)))

    def load(self, rows: List[str]):
        # TODO: вызвать submit(row) для каждой строки
        for row in rows:
            self.submit(row)

    def client_totals(self) -> Dict[str, int]:
        # TODO: собрать dict вида client -> total_reserved_quantity
        result = {}
        for r in self.accepted:
            result[r.client] = result.get(r.client, 0) + r.quantity
        return result

    def top_client(self):
        # TODO: использовать client_totals()
        totals = self.client_totals()
        if not totals:
            return None

        # TODO: вернуть tuple(client, total_quantity) с максимумом
        return max(totals.items(), key = lambda x: x[1])

    def lowest_stock_warehouse(self):
        # TODO: найти склад с минимумом total_left()
        if not self.warehouses:
            return None
        w = min(self.warehouses.values(), key = lambda w: w.total_left())

        # TODO: вернуть tuple(warehouse_id, total_left)
        return (w.warehouse_id, w.total_left())

    def warehouse_snapshot(self):
        # TODO: собрать dict вида warehouse_id -> копия текущих остатков products
        return {wid: dict(w.products) for wid, w in self.warehouses.items()}

    def find_request(self, request_id: str) -> Optional[ReservationRequest]:
        # TODO: вернуть Optional[ReservationRequest]
        # TODO: пройтись по self.accepted и найти нужную заявку
        for r in self.accepted:
            if r.request_id == request_id:
                return r
            
        # TODO: если не найдено -> вернуть None
        return None


service = ReservationService(stocks)

# TODO: загрузить rows через service.load(rows)
service.load(rows)

# TODO: вывести принятые заявки
print("Принятые заявки:")
for r in service.accepted:
    print(r)

# TODO: вывести ошибки
print("\nЖурнал ошибок:")
for e in service.errors:
    print(e)

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