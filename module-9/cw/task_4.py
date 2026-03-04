lines = [
    "P-1;Mouse;25;Periphery",
    "P-2;Keyboard;45;Periphery",
    "P-3;Cloud VM;120;Services",
    "P-2;Duplicate;50;Periphery",
    "P-4;Broken;-5;Services",
    "P-5;BadPrice;abc;Services",
]


def is_number(text):
    # TODO: вернуть True, если text можно считать числом (включая дроби и знак), иначе False
    text = text.strip()
    if not text: return False
    return text.replace('.', '', 1).replace('-', '', 1).isdigit()


class Product:
    # TODO: __init__(id, name, price, category)
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self._price = float(price)
        self.category = category
    # TODO: property price (только getter)
    @property
    def price(self):
        return self._price
    # TODO: set_price(value) -> bool
    def set_price(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._price = float(value)
            return True
        return False
    # TODO: classmethod from_line(cls, raw) -> (product_or_none, reason)
    @classmethod
    def from_line(cls, raw):
        parts = [p.strip() for p in raw.split(';')]
        if len(parts) != 4:
            return None, "Неверный формат (нужно 4 поля)"
        
        p_id, name, price_str, category = parts

        if not is_number(price_str):
            return None, "Цена не является числом"
        
        price = float(price_str)
        if price < 0:
            return None, "Отрицательная цена"
        
        return cls(p_id, name, price, category), ""


class ProductRegistry:
    # TODO: __init__ (products list + id set)
    def __init__(self):
        self.products = []
        self.ids = set()
    # TODO: add(product) -> (bool, reason)
    def add(self, product):
        if product.id in self.ids:
            return False, "Дубликат ID"
        self.products.append(product)
        self.ids.add(product.id)
        return True, ""
    # TODO: count()
    def count(self):
        return len(self.products)
    # TODO: all_products()
    def all_products(self):
        return self.products
    # TODO: has_id(id)
    def has_id(self, p_id):
        return p_id in self.ids
    # TODO: by_category()
    def by_category(self):
        stats = {}
        for p in self.products:
            stats[p.category] = stats.get(p.category, 0) + 1
        return stats
    # TODO: avg_price()
    def avg_price(self):
        if not self.products:
            return 0
        total = sum(p.price for p in self.products)
        return total / len(self.products)


# TODO: создать registry и problems
registry = ProductRegistry()
problems = []
# TODO: пройти по lines, загрузить валидные товары
for line in lines:
    product, reason = Product.from_line(line)
    if product:
        success, add_reason = registry.add(product)
        if not success:
            problems.append((line, add_reason))
# TODO: проблемные строки добавлять в problems как (line, reason)
for line, reason in problems:
    print(f"[{reason}]: {line}")
# TODO: вывести count, by_category, avg_price и problems
print(f"Валидных товаров: {registry.count()}")
print(f"Статистика по категориям: {registry.by_category()}")
print(f"Средняя цена: {registry.avg_price():.2f}")