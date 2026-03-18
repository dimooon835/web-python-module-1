# rows: pass_id|member_name|plan|days_left|status
rows = [
    'PS-100|Alice|flex|12|active',
    'PS-101|Bob|fixed|20|paused',
    'PS-102|Team Rocket|team|0|expired',
    'PS-103|Diana|flex|6|active',
]


class CoworkingPass:
    allowed_plans = {'flex', 'fixed', 'team'}
    allowed_statuses = {'active', 'paused', 'expired'}

    def __init__(self, pass_id, member_name, plan, days_left, status):
        # TODO: проверить plan и status, иначе raise ValueError(...)
        if plan not in self.allowed_plans:
            raise ValueError(f"Неправильный план: {plan}")
        if status not in self.allowed_statuses:
            raise ValueError(f"Неправильный статус: {status}")
        
        # TODO: сохранить pass_id, member_name, plan, status
        self.pass_id = pass_id
        self.member_name = member_name
        self.plan = plan
        self.status = status

        # TODO: days_left хранить через внутреннее поле self._days_left
        # TODO: значение days_left пропустить через property/setter
        self.days_left = days_left

    @property
    def days_left(self):
        # TODO: вернуть текущее число оставшихся дней
        return self._days_left

    @days_left.setter
    def days_left(self, value):
        # TODO: привести value к int
        value = int(value)

        # TODO: если value < 0 -> raise ValueError('Days must be >= 0')
        if value < 0:
            raise ValueError(f"Дни должны быть больше или равны 0")

        # TODO: сохранить результат в self._days_left
        self._days_left = value

    def use_day(self):
        # TODO: если статус не 'active' -> raise ValueError(...)
        if self.status != 'active':
            raise ValueError(f"Статус не активен")
        
        # TODO: если days_left == 0 -> raise ValueError(...)
        if self.days_left == 0:
            raise ValueError(f"Не осталось дней")

        # TODO: уменьшить days_left на 1
        self.days_left -= 1

        # TODO: если после списания days_left == 0, перевести статус в 'expired'
        if self.days_left == 0:
            self.status = 'expired'

    def pause(self):
        # TODO: если статус 'expired' -> raise ValueError(...)
        if self.status == 'expired':
            raise ValueError(f"Статус завершён")

        # TODO: перевести пропуск в 'paused'
        self.status = 'paused'

    def resume(self):
        # TODO: если days_left == 0 -> raise ValueError(...)
        if self.days_left == 0:
            raise ValueError(f"Не осталось дней")
        
        # TODO: перевести пропуск в 'active'
        self.status = 'active'

    def renew(self, extra_days):
        # TODO: привести extra_days к int
        extra_days = int(extra_days)

        # TODO: если extra_days <= 0 -> raise ValueError(...)
        if extra_days <= 0:
            raise ValueError(f"Экстра дни должны быть больше 0")

        # TODO: увеличить days_left
        self.days_left += extra_days

        # TODO: если days_left > 0 и статус был 'expired', перевести в 'active'
        was_expired = self.status == 'expired'
        if was_expired and self.days_left > 0:
            self.status = 'active'

    @classmethod
    def from_row(cls, row):
        # TODO: split по '|'
        parts = row.split('|')

        # TODO: ожидать 5 частей: pass_id, member_name, plan, days_left, status
        if len(parts) !=5:
            raise ValueError(f"Неправильный формат")
        pass_id, member_name, plan, days_left, status = parts
        
        # TODO: вернуть CoworkingPass(...)
        return cls(pass_id, member_name, plan, days_left, status)

    def __repr__(self):
        # TODO: вернуть строку вида CoworkingPass(pass_id='...', member_name='...', status='...', days_left=...)
        return (f"CoworkingPass(pass_id='{self.pass_id}', member_name='{self.member_name}', plan='{self.plan}', status='{self.status}', days_left={self.days_left}")


class CoworkingRegistry:
    def __init__(self):
        self.items = []

    def add(self, coworking_pass):
        # TODO: добавить объект в self.items
        self.items.append(coworking_pass)

    def load(self, rows):
        # TODO: для каждой строки создать CoworkingPass.from_row(row)
        for row in rows:
            cp = CoworkingPass.from_row(row)

        # TODO: добавить объект в реестр через add(...)
        self.add(cp)
        

    def active_passes(self):
        # TODO: вернуть список пропусков со статусом 'active'
        return [p for p in self.items if p.status == 'active']

    def by_plan(self, plan):
        # TODO: вернуть список пропусков нужного тарифа
        return [p for p in self.items if p.plan == plan]

    def total_days_left(self):
        # TODO: вернуть суммарное число оставшихся дней
        return sum(p.days_left for p in self.items)

    def status_summary(self):
        # TODO: собрать dict вида status -> count
        summary = {}
        for p in self.items:
            summary[p.status] = summary.get(p.status, 0) + 1
        return summary

    def find(self, pass_id):
        # TODO: вернуть пропуск по pass_id или None
        for p in self.items:
            if p.pass_id == pass_id:
                return p
        return None

    def largest_balance(self):
        # TODO: найти пропуск с максимальным days_left
        if not self.items:
            return None
        p = max(self.items, key=lambda x: x.days_left)

        # TODO: вернуть tuple(pass_id, days_left)
        return (p.pass_id, p.days_left)


registry = CoworkingRegistry()

# TODO: загрузить rows в registry
registry.load(rows)

# TODO: вывести все пропуска
print("Все пропуска:")
for p in registry.items:
    print(p)

# TODO: вывести active_passes()
print("\nАктивные:")
print(registry.active_passes())

# TODO: вывести by_plan('flex')
print("\nПо плану flex:")
print(registry.by_plan('flex'))

# TODO: вывести total_days_left()
print("\nСумма дней:")
print(registry.total_days_left())

# TODO: вывести status_summary()
print("\nСводка статусов:")
print(registry.status_summary())

# TODO: найти пропуск 'PS-101', возобновить его и вывести status_summary()
p = registry.find("PS-101")
p.resume()
print("\nПосле возобновления PS-101:")
print(registry.status_summary())

# TODO: найти пропуск 'PS-100', списать один день и вывести объект
p = registry.find("PS-100")
p.use_day()
print("\nПосле списания PS-100:")
print(p)

# TODO: найти пропуск 'PS-102', продлить на 5 дней и вывести объект
p = registry.find("PS-102")
p.renew(5)
print("\nПосле продление PS-102:")
print(p)

# TODO: вывести largest_balance()
print("\nМаксимальный баланс:")
print(registry.largest_balance())