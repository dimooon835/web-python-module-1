rows = [
    'S-100,Acme,12.5,express,RU',
    'S-101,Beta,0,standard,RU',
    'S-102,Acme,abc,vip,KZ',
    'S-103,Delta,8.5,urgent,BY',
    'S-104,Gamma,15,vip,UZ',
    'S-105,Acme,4.0,standard,KZ',
    'S-106,Beta,9.5,express,BY',
]


class ShipmentError(Exception):
    pass


class RowFormatError(ShipmentError):
    pass


class WeightError(ShipmentError):
    pass


class PriorityError(ShipmentError):
    pass


class RegionError(ShipmentError):
    pass


def parse_shipment(row):
    # TODO: распарсить строку и провалидировать weight, priority, region
    parts = row.split(',')
    if len(parts) !=5:
        raise RowFormatError(f"Не 5 элементов, а {len(parts)}")
    
    s_id, client, weight_str, priority, region = parts

    try:
        weight = float(weight_str)
    except ValueError as e:
        raise WeightError(f"Вес '{weight_str}' не является числом") from e
    
    if weight <= 0:
        raise WeightError(f"Вес должен быть > 0 (получено {weight})")
    
    if priority not in ['standard', 'express', 'vip']:
        raise PriorityError(f"Неизвестный приоритет: {priority}")
    
    if region not in ['RU', 'KZ', 'BY']:
        raise RegionError(f"Неизвестный регион: {region}")

    # TODO: при ошибке конвертации weight использовать raise ... from ...
    return {'id': s_id, 'client': client, 'weight': weight, 'priority': priority, 'region': region}

def load_shipments(rows):
    # TODO: вернуть (shipments, errors)
    shipments = []
    errors = []
    for row in rows:
        try:
            shipments.append(parse_shipment(row))
        except ShipmentError as e:
            errors.append((row, type(e).__name__, str(e)))
    return shipments, errors


# TODO: вызвать load_shipments(rows)
valid_data, error_log = load_shipments(rows)

# TODO: вывести число валидных отгрузок и число ошибок
premium_weight = sum(s['weight'] for s in valid_data if s['priority'] in ['express', 'vip'])
client_weights = {}
error_counts = {}

# TODO: вывести ошибки по типам
for _, err_type, _ in error_log:
    error_counts[err_type] = error_counts.get(err_type, 0) + 1

for s in valid_data:
    name = s['client']
    client_weights[name] = client_weights.get(name, 0) + s['weight']

print(f"Валидные отгрузки: {len(valid_data)}")
print(f"Ошибки: {len(error_log)} {error_counts}")

leader = max(client_weights, key=client_weights.get) if client_weights else None

# TODO: посчитать premium_weight только для express/vip
print(f"Суммарный вес: {premium_weight}")

# TODO: найти клиента-лидера по суммарному весу
leader = max(client_weights, key=client_weights.get)
print(f"Клиент-лидер: {leader} ({client_weights[leader]} кг)")