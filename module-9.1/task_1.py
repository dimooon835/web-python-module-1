from collections import Counter, defaultdict

rows = [
    'INV-100,Keyboard,3,120,paid',
    'INV-101,Mouse,0,40,new',
    'INV-102,Monitor,2,abc,approved',
    'INV-103,Laptop,1,1400,shipped',
    'INV-104,Keyboard,5,110,paid',
    'INV-105,Dock,2,-50,approved',
]


class InvoiceError(Exception):
    pass


class RowFormatError(InvoiceError):
    pass


class QuantityError(InvoiceError):
    pass


class PriceError(InvoiceError):
    pass


class StatusError(InvoiceError):
    pass


def parse_invoice(row):
    # TODO: распарсить строку и провалидировать quantity, price, status
    # TODO: при ошибках конвертации использовать raise ... from ...
    parts = [p.strip() for p in row.split(',')]
    if len(parts) != 5:
        raise RowFormatError("Не 5 элементов")

    inv_id, item, qty_raw, price_raw, status = parts

    try:
        quantity = int(qty_raw)
    except ValueError as e:
        raise QuantityError(f"Quantity '{qty_raw}' не является целым числом") from e
    if quantity <= 0:
        raise QuantityError(f"Quantity {quantity} должно быть больше > 0")

    try:
        price = float(price_raw)
    except ValueError as e:
        raise PriceError(f"Price '{price_raw}' не является числом") from e
    if price < 0:
        raise PriceError(f"Price {price} не может быть отрицательной")
    
    if status not in ["new", "approved", "paid"]:
        raise StatusError(f"Недопустимый статус: {status}")
    
    return {
        "id": inv_id,
        "item": item,
        "quantity": quantity,
        "price": price,
        "status": status
    }

def load_invoices(rows):
    # TODO: вернуть (invoices, errors)
    invoices = []
    errors = []

    for row in rows:
        try:
            inv = parse_invoice(row)
            invoices.append(inv)
        except InvoiceError as e:
            errors.append((row, type(e).__name__, str(e)))

    return invoices, errors

# TODO: вызвать load_invoices(rows)
# TODO: вывести число валидных накладных и число ошибок
# TODO: вывести ошибки по типам
# TODO: посчитать paid_total
# TODO: найти товар-лидер по количеству

valid_invoices, error_list = load_invoices(rows)

error_types = Counter(err[1] for err in error_list)
paid_total = sum(inv["price"] * inv["quantity"] for inv in valid_invoices if inv["status"] == "paid")

item_counts = defaultdict(int)
for inv in valid_invoices:
    item_counts[inv["item"]] += inv["quantity"]
leader = max(item_counts.items(), key = lambda x: x[1]) if item_counts else (None, 0)

print(f"Валидных записей: {len(valid_invoices)}")
print(f"Ошибки по типам: {dict(error_types)}")
print(f"Сумма оплаченных: {paid_total:.2f}")
print(f"Товар-лидер: {leader[0]} (кол-во: {leader[1]})")