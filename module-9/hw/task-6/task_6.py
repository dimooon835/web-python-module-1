from dataclasses import dataclass
from typing import Optional


couriers = {
    'CR-1': {'zone': 'north', 'charge_min': 40, 'max_weight': 3.0},
    'CR-2': {'zone': 'south', 'charge_min': 30, 'max_weight': 2.0},
    'CR-3': {'zone': 'north', 'charge_min': 55, 'max_weight': 5.0},
}

# rows: delivery_id|courier_id|client|weight_kg|route_min
rows = [
    'DL-100|CR-1|Clinic|1.5|12',
    'DL-101|CR-2|Cafe|2.5|10',
    'DL-102|CR-9|Lab|1.0|8',
    'DL-103|CR-1|Shop|0|6',
    'DL-104|CR-3|Village|3.5|60',
    'DL-100|CR-3|Clinic|1.0|10',
    'DL-105|CR-3|School|2.0|20',
    'DL-106|CR-2|Pharmacy|1.0|15',
]


class DeliveryError(Exception):
    pass


class RowFormatError(DeliveryError):
    pass


class CourierNotFoundError(DeliveryError):
    pass


class WeightError(DeliveryError):
    pass


class RouteTimeError(DeliveryError):
    pass


class WeightLimitError(DeliveryError):
    pass


class ChargeReserveError(DeliveryError):
    pass


class DuplicateDeliveryError(DeliveryError):
    pass


@dataclass(order=True)
class Delivery:
    route_min: int
    delivery_id: str
    courier_id: str
    client: str
    weight_kg: float


class Courier:
    def __init__(self, courier_id, zone, charge_min, max_weight):
        # TODO: сохранить courier_id, zone, charge_min, max_weight
        # TODO: создать список deliveries
        self.courier_id = courier_id
        self.zone = zone
        self.charge_min = charge_min
        self.max_weight = max_weight
        self.deliveries = []

    def charge_left(self):
        # TODO: вернуть текущий остаток заряда в минутах
        return self.charge_min - self.total_route_time()

    def total_route_time(self):
        # TODO: вернуть сумму route_min по self.deliveries
        return sum(d.route_min for d in self.deliveries)

    def total_weight(self):
        # TODO: вернуть сумму weight_kg по self.deliveries
        return sum(d.weight_kg for d in self.deliveries)

    def assign(self, delivery):
        # TODO: если delivery.weight_kg > self.max_weight -> raise WeightLimitError(...)
        # TODO: посчитать charge_after = charge_left() - delivery.route_min
        # TODO: если charge_after < 5 -> raise ChargeReserveError(...)
        # TODO: добавить delivery в self.deliveries
        # TODO: отсортировать self.deliveries
        if delivery.weight_kg > self.max_weight:
            raise WeightLimitError(f"Weight {delivery.weight_kg} превышает максимум {self.max_weight}")
        
        charge_after = self.charge_left() - delivery.route_min
        if charge_after < 5:
            raise ChargeReserveError(f"Charge слишком низкий: {charge_after} мин")
            
        self.deliveries.append(delivery)
        self.deliveries.sort()


class CourierDispatchService:
    def __init__(self, couriers):
        # TODO: создать couriers вида courier_id -> Courier(...)
        # TODO: создать списки accepted и errors
        # TODO: создать множество processed_ids
        self.couriers = {cid: Courier(cid, **data) for cid, data in couriers.items()}
        self.accepted = []
        self.errors = []
        self.processed_ids = set()

    def parse_delivery(self, row):
        # TODO: split по '|'
        # TODO: ожидать 5 частей: delivery_id, courier_id, client, weight_raw, route_raw
        # TODO: если частей не 5 -> raise RowFormatError(...)
        # TODO: проверить, что courier_id существует
        # TODO: weight_raw преобразовать в float
        # TODO: route_raw преобразовать в int
        # TODO: ошибки преобразования поднимать через WeightError / RouteTimeError с raise ... from exc
        # TODO: если weight_kg <= 0 -> raise WeightError(...)
        # TODO: если route_min <= 0 -> raise RouteTimeError(...)
        # TODO: вернуть Delivery(...)
        parts = row.split('|')
        if len(parts) != 5:
            raise RowFormatError("Неправильный формат")
            
        d_id, c_id, client, w_raw, r_raw = parts
        
        if c_id not in self.couriers:
            raise CourierNotFoundError(f"Courier {c_id} не найден")
            
        try:
            weight_kg = float(w_raw)
        except ValueError as e:
            raise WeightError(f"Неверный weight: {w_raw}") from e
            
        try:
            route_min = int(r_raw)
        except ValueError as e:
            raise RouteTimeError(f"Неверный route time: {r_raw}") from e
            
        if weight_kg <= 0:
            raise WeightError("Weight должен быть положительным")
        if route_min <= 0:
            raise RouteTimeError("Route time должен быть положительным")
            
        return Delivery(route_min, d_id, c_id, client, weight_kg)

    def submit(self, row):
        # TODO: внутри try вызвать parse_delivery(row)
        # TODO: если delivery.delivery_id уже в processed_ids -> raise DuplicateDeliveryError(...)
        # TODO: передать delivery в couriers[delivery.courier_id].assign(delivery)
        # TODO: после успеха обновить processed_ids и accepted
        # TODO: DeliveryError сохранить в errors как (row, error_type, message)
        try:
            delivery = self.parse_delivery(row)
            if delivery.delivery_id in self.processed_ids:
                raise DuplicateDeliveryError(f"Delivery {delivery.delivery_id} уже существует")
            
            self.couriers[delivery.courier_id].assign(delivery)
            self.processed_ids.add(delivery.delivery_id)
            self.accepted.append(delivery)
        except DeliveryError as e:
            self.errors.append((row, type(e).__name__, str(e)))

    def load(self, rows):
        # TODO: вызвать submit(row) для каждой строки
        for row in rows:
            self.submit(row)

    def client_weights(self):
        # TODO: собрать dict вида client -> total_weight_kg
        weights = {}
        for d in self.accepted:
            weights[d.client] = weights.get(d.client, 0) + d.weight_kg
        return weights

    def top_client(self):
        # TODO: использовать client_weights()
        # TODO: вернуть tuple(client, weight_kg) с максимумом
        weights = self.client_weights()
        if not weights: return None
        client = max(weights, key=weights.get)
        return (client, weights[client])

    def busiest_courier(self):
        # TODO: найти курьера с максимумом total_route_time()
        # TODO: вернуть tuple(courier_id, total_route_time)
        c = max(self.couriers.values(), key=lambda x: x.total_route_time())
        return (c.courier_id, c.total_route_time())

    def low_charge_couriers(self, threshold=15):
        # TODO: вернуть список tuple(courier_id, charge_left)
        # TODO: включать только курьеров, у которых charge_left() <= threshold
        return [(c.courier_id, c.charge_left()) for c in self.couriers.values() if c.charge_left() <= threshold]

    def find_delivery(self, delivery_id):
        # TODO: пройтись по всем курьерам и их доставкам
        # TODO: если delivery.delivery_id совпал -> вернуть объект Delivery
        # TODO: если доставка не найдена -> вернуть None
        for courier in self.couriers.values():
            for delivery in courier.deliveries:
                if delivery.delivery_id == delivery_id:
                    return delivery
        return None


service = CourierDispatchService(couriers)

# TODO: загрузить rows через service.load(rows)
# TODO: вывести принятые доставки
# TODO: вывести ошибки
# TODO: вывести по каждому курьеру deliveries, total_route_time и charge_left
# TODO: вывести top_client()
# TODO: вывести busiest_courier()
# TODO: вывести low_charge_couriers()
# TODO: вывести find_delivery('DL-105')
        
service.load(rows)

print("Принятые доставки:", [d.delivery_id for d in service.accepted])

print("\nЖурнал ошибок:")
for err in service.errors: print(f"  {err}")

print("\nСтатус курьеров:")
for cid, c in service.couriers.items():
    print(f"  {cid}: Доставок {len(c.deliveries)}. Время {c.total_route_time()} мин. Остаток заряда {c.charge_left()} мин")

print(f"\nТоп клиент: {service.top_client()}")

print(f"Самый загруженный курьер: {service.busiest_courier()}")

print(f"Самый низкий заряд: {service.low_charge_couriers()}")

print(f"Поиск DL-105: {service.find_delivery('DL-105')}")