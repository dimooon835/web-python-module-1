devices_data = [
    ("D-1", "MacBook Pro", "laptop", 45, True),
    ("D-2", "iPad Air", "tablet", 25, True),
    ("D-3", "Canon R50", "camera", 40, True),
    ("D-2", "Duplicate iPad", "tablet", 30, True)
]

rental_ops = [
    ("Алиса", "D-1", 3),
    ("Боб", "D-2", 2),
    ("Кира", "D-2", 4),
    ("Данил", "D-9", 1),
    ("Ева", "D-3", 0)
]


class Device:
    # TODO:
    # реализуй __init__(device_id, title, device_type, daily_price, available)
    def __init__(self, device_id, title, device_type, daily_price, available):
        self.device_id = device_id
        self.title = title
        self.device_type = device_type
        self._daily_price = daily_price
        self.available = available

    @property
    def daily_price(self):
        # TODO:
        # вернуть текущую цену аренды
        return self._daily_price

    def set_daily_price(self, value):
        # TODO:
        # если value > 0:
        #    обновить цену и вернуть True
        # иначе вернуть False
        if value > 0:
            self.daily_price = value
            return True
        return False
            

    def to_dict(self):
        # TODO:
        # вернуть словарь с полями device_id, title, device_type, daily_price, available
        return {
            "device_id": self.device_id,
            "title": self.title,
            "device_type": self.device_type,
            "daile_price": self.daily_price,
            "available": self.available
        }



class RentalRegistry:
    def __init__(self):
        # TODO:
        self.devices = {}
        self.rentals = []
        self.problems = []

    def add_device(self, device):
        # TODO:
        # если device.device_id уже есть:
        #    добавить (device.device_id, "duplicate device") в self.problems
        # иначе сохранить устройство
        if device.device_id in self.devices:
            self.problems.append((device.device_id, "duplicate device"))
        else:
            self.devices[device.device_id] = device

    def rent(self, employee, device_id, days):
        # TODO:
        # 1) проверить, что устройство существует
        # 2) проверить, что days > 0
        # 3) проверить, что device.available == True
        # 4) если всё хорошо:
        #    total_price = device.daily_price * days
        #    добавить словарь аренды в self.rentals
        #    device.available = False
        if device_id not in self.devices:
            self.problems.append((device_id, "device not found"))
            return
        
        device = self.devices[device_id]

        if days <= 0:
            self.problems.append((device_id, "invalid days"))
            return
        
        if not device.available:
            self.problems.append((device_id, "device busy"))
            return
        
        total_price = device.daily_price * days
        self.rentals.append({
            "employee": employee,
            "device_id": device_id,
            "device_type": device.device_type,
            "income": total_price
        })
        device.available = False

    def return_device(self, device_id):
        # TODO:
        # если device_id нет -> добавить проблему
        # иначе -> self.devices[device_id].available = True
        if device_id not in self.devices:
            self.problems.append((device_id, "return failed: device_id not found"))
        else:
            self.devices[device_id].available = True

    def income_by_type(self):
        # TODO:
        # вернуть словарь {device_type: total_income}
        income_map = {}
        for r in self.rentals:
            d_type = r['device_type']
            income_map[d_type] = income_map.get(d_type, 0) + r['income']
        return income_map

    def busy_devices(self):
        # TODO:
        # вернуть список занятых устройств
        return [d.title for d in self.devices.values() if not d.available]

    def build_report(self):
        # TODO:
        # вернуть словарь с ключами:
        # total_devices, total_rentals, total_income,
        # income_by_type, busy_devices, problems
        income_types = self.income_by_type()
        return {
            "total_devices": len(self.devices),
            "total_rentals": len(self.rentals),
            "total_income": sum(income_types.values()),
            "income_by_type": income_types,
            "busy_devices": self.busy_devices(),
            "problems": self.problems
        }


registry = RentalRegistry()

for row in devices_data:
    # TODO:
    # создать Device(*row) и добавить в registry
    dev = Device(row[0], row[1], row[2], row[3], row[4])
    registry.add_device(dev)

for employee, device_id, days in rental_ops:
    # TODO:
    # вызвать registry.rent(employee, device_id, days)
    registry.rent(employee, device_id, days)

report = registry.build_report()

print("Устройств:", report["total_devices"])
print("Успешных аренд:", report["total_rentals"])
print("Доход:", report["total_income"])
print("Доход по типам:", report["income_by_type"])
print("Занятые устройства:", report["busy_devices"])
print("Проблемы:", report["problems"])