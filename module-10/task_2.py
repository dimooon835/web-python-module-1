wallets = {
    'alice': {'currency': 'USD', 'balance': 1200.0},
    'bob': {'currency': 'USD', 'balance': 450.0},
    'carol': {'currency': 'EUR', 'balance': 900.0},
    'dave': {'currency': 'USD', 'balance': 150.0},
}

rows = [
    'TR-100|alice|bob|200',
    'TR-101|bob|dave|700',
    'TR-102|alice|carol|50',
    'TR-103|eve|bob|30',
    'TR-104|dave|dave|10',
    'TR-105|bob|alice|abc',
    'TR-106|bob|dave|100',
]


class TransferError(Exception):
    pass


class TransferFormatError(TransferError):
    pass


class AccountNotFoundError(TransferError):
    pass


class CurrencyMismatchError(TransferError):
    pass


class InsufficientFundsError(TransferError):
    pass


class TransferAmountError(TransferError):
    pass


def parse_transfer(raw):
    # TODO: распарсить строку и вернуть dict перевода
    # TODO: при ошибке конвертации amount использовать raise ... from ...
    try:
        parts = raw.split('|')
        if len(parts) != 4:
            raise TransferFormatError(f"Не 4 элемента, а {len(parts)}")
        
        tid, sender, receiver, amount_str = parts

        try:
            amount = float(amount_str)
        except ValueError as e:
            raise TransferFormatError(f"Неправильное значение: {amount_str}") from e
    
        return {
            "id": tid,
            "from": sender,
            "to": receiver,
            "amount": amount
        }
    except Exception as e:
        if not isinstance(e, TransferError):
            raise TransferFormatError(str(e)) from e
        raise

def apply_transfer(transfer, wallets):
    # TODO: проверить существование аккаунтов
    # TODO: запретить перевод самому себе
    # TODO: проверить совпадение валют
    # TODO: проверить баланс отправителя
    # TODO: обновить балансы и вернуть dict результата
    s_id, r_id = transfer["from"], transfer["to"]
    amt = transfer["amount"]

    if s_id not in wallets or r_id not in wallets:
        missing = s_id if s_id not in wallets else r_id
        raise AccountNotFoundError(f"Пользователя '{missing}' не существует")
    
    if s_id == r_id:
        raise TransferError(f"Нельзя переводить самому себе")

    if wallets[s_id]["currency"] != wallets[r_id]["currency"]:
        raise CurrencyMismatchError(f"Валюты не совпадают: {wallets[s_id]["currency"]} против {wallets[r_id]["currency"]}")
    
    if wallets[s_id]["balance"] < amt:
        raise InsufficientFundsError(f"Не хватает средств: {wallets[s_id]["balance"]} < {amt}")
    
    wallets[s_id]["balance"] -= amt
    wallets[r_id]["balance"] += amt
    return {"id": transfer["id"], "status": "success"}

def process_batch(rows, wallets):
    # TODO: вернуть (successes, errors)
    successes = []
    errors = []
    for row in rows:
        try:
            transfer_data = parse_transfer(row)
            result = apply_transfer(transfer_data, wallets)
            successes.append(result)
        except TransferError as e:
            errors.append((row, type(e).__name__, str(e)))
    return successes, errors

# TODO: вызвать process_batch(rows, wallets)
# TODO: вывести успешные переводы
# TODO: вывести ошибки по типам
# TODO: вывести итоговые балансы
# TODO: найти richest_usd_user

success_list, errors_list = process_batch(rows, wallets)

print("Успешные переводы")
for s in success_list:
    print(f"Обработан: {s["id"]}")

print("\nОшибки по типам")
for raw, err_type, msg in errors_list:
    print(f"[{err_type}] Строка: {raw} | Ошибка: {msg}")

print("\nИтоговые балансы")
for name, data in wallets.items():
    print(f"{name}: {data["balance"]} {data["currency"]}")

usd_users = {u: d["balance"] for u, d in wallets.items() if d["currency"] == "USD"}
richest = max(usd_users, key = usd_users.get)

print(f"Самый богатый (USD): {richest} ({wallets[richest]["balance"]} USD)")