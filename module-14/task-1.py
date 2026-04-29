from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Ingredient:
    name: str
    key: str
    price: float
    cost: float

@dataclass
class Recipe:
    name: str
    ingredient_keys: list[str]

class RecipeFactory:
    def get_standard_recipes() -> dict[int, Recipe]:
        return {
            0: Recipe("РџРёС†С†Р°-1", ["dough", "cheese", "tomate", "mayonnaise", "chiken"]),
            1: Recipe("РџРёС†С†Р°-2", ["dough", "cheese", "tomate", "ketchup", "chiken"]),
            2: Recipe("РџРёС†С†Р°-3", ["dough", "cheese", "tomate", "chiken"])
        }
    

class PizzaBuilder:
    def __init__(self):
        self._ingredient = ["dough", "cheese"]

    def add_ingredient(self, key: str):
        if key not in self._ingredient:
            self._ingredient.append(key)
        return self
    
    def build(self):
        return Recipe("РЎРІРѕСЏ РїРёС†С†Р°", self._ingredient)
    

# ----------
@dataclass
class OrderItem:
    recipe: Recipe
    quantity: int

    def total_price(self, ingredients: dict[int, Ingredient]) -> float:
        one_pizza_price = sum(
            ingredients[key].price for key in self.recipe.ingredient_keys
        )

        return one_pizza_price * self.quantity
    
    def total_cost(self, ingredients: dict[int, Ingredient]) -> float:
        one_pizza_cost = sum(
            ingredients[key].cost for key in self.recipe.ingredient_keys
        )

        return one_pizza_cost * self.quantity

@dataclass
class Order:
    items: list[OrderItem]
    payment_type: str

    def total_price(self, ingredients: dict[str, Ingredient]):
        return sum(item.total_price(ingredients) for item in self.items)
    
    def total_cost(self, ingredients: dict[str, Ingredient]):
        return sum(item.total_cost(ingredients) for item in self.items)

    def total_profit(self, ingredients: dict[str, Ingredient]):
        return self.total_price(ingredients) - self.total_cost(ingredients)

    def to_text(self, ingredients: dict[str, Ingredient]) -> str:
        lines = ["РРЅС„РѕСЂРјР°С†РёСЏ Рѕ Р·Р°РєР°Р·Рµ:"]

        for item in self.items:
            ingredients_names = [
                ingredients[key].name for key in item.recipe.ingredient_keys
            ]

            lines.append(f"РџРёС†С†Р°: {item.recipe.name}")
            lines.append(f"РљРѕР»РёС‡РµСЃС‚РІРѕ: {item.quantity}")
            lines.append("РЎРѕСЃС‚Р°РІ:")

            for name in ingredients_names:
                lines.append(f"- {name}")

            lines.append(f"Р¦РµРЅР° РїРѕР·РёС†РёРё: {item.total_price(ingredients)} СЂСѓР±.")
        
        lines.append(f"РЎРїРѕСЃРѕР± РѕРїР»Р°С‚С‹: {self.payment_type}")

        return "\n".join(lines)
    
# ----------
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class CashPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"РћРїР»Р°С‚Р° РЅР°Р»РёС‡РЅС‹РјРё РІС‹РїРѕР»РЅРµРЅР° РЅР° СЃСѓРјРјСѓ {amount} СЂСѓР±."
    
class CardPayment(PaymentStrategy):
    def pay(self, amount: float):
        return f"РћРїР»Р°С‚Р° РєР°СЂС‚РѕР№ РІС‹РїРѕР»РЅРµРЅР° РЅР° СЃСѓРјРјСѓ {amount} СЂСѓР±."
    
# ----------

class FileOrderSaver:
    def __init__(self, filename: str = "order.txt"):
        self.filename = filename

    def save(self, order: Order, ingredients: dict[str, Ingredient]):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(order.to_text(ingredients))
            file.write("\n" + "-" * 50 + "\n")


def create_ingredients():
    return {
        "dough": Ingredient("РўРµСЃС‚Рѕ", "dough", 70, 30),
        "cheese": Ingredient("РЎС‹СЂ", "cheese", 80, 20),
        "tomate": Ingredient("РџРѕРјРёРґРѕСЂ", "tomate", 20, 5),
        "mayonnaise": Ingredient("РњР°Р№РѕРЅРµР·", "mayonnaise", 50, 10),
        "chiken": Ingredient("РљСѓСЂРёС†Р°", "chiken", 100, 50),
        "ketchup":Ingredient("РљРµС‚С‡СѓРї", "ketchup", 15, 3),
    }

def create_stock() -> dict[str, int]:
    return {
        "dough": 10,
        "cheese": 10,
        "tomate": 10,
        "mayonnaise": 10,
        "chiken": 10,
        "ketchup": 10
    }

def get_topping() -> list[str]:
    return [
        "tomate",
        "mayonnaise",
        "chiken",
        "ketchup"
    ]

def create_custom_recipe(inventory: Inventory) -> Recipe:
    buider = PizzaBuilder()

    print("Создание своей пиццы")
    for key in get_topping():
        ingredient = inventory.ingredients[key]

        choice = input("Хотите добавить {ingredient.name}") # Да/Нет
        if choice == "да":
            buider.add_ingredient(ingredient.key)

    return buider.build()

# ----------

class Inventory:
    def __init__(self, ingredients: dict[str, Ingredient], stock: dict[str, int]):
        self.ingredients = ingredients
        self.stock = stock

    def has_enough(self, ingredient_keys: list[str], quantity: int) -> bool:
        for key in ingredient_keys:
            if self.stock.get(key, 0) < quantity:
                return False
        return True
    
    def reduce_stock(self, ingredient_keys: list[str], quantity: int):
        for key in ingredient_keys:
            self.stock[key] -= quantity

    def show(self):
        print("Наличие ингредиентов")
        
        for key, count in self.stock.items():
            ingredient = self.ingredients[key]
            print(f"{ingredient.name}: {count}")

# ----------

class SalesReport:
    def __init__(self):
        self.profit = 0
        self.revenue = 0
        self.sold_count = 0

    def add_order(self, order: Order, ingredients: dict[str, Ingredient]):
        self.sold_count += sum(item.quantity for item in order.items)
        self.revenue += order.total_price(ingredients)
        self.profit += order.total_profit(ingredients)

    def show(self):
        print("Отчёт")
        print(f"Прожано пицц: {self.sold_count}")
        print(f"Выручка: {self.profit}")
        print(f"Доход: {self.revenue}")

def show_menu():
    print("1. Создать заказ")
    print("2. Отчёт")
    print("3. Наличие ингредиентов")
    print("4. Выход")

def show_standard_recipes(
        recipes: dict[int, Recipe],
        ingredients: dict[str, Ingredient]):
    print("Стандартные рецепты")

    for number, recipe in recipes.items():
        print(f"{number}, {recipe.name}")

    price = sum(ingredients[key].price for key in recipe.ingredient_keys)
    print(f"Цена за штуку: {price}")

def choose_recipe(
        recipes: dict[int, Recipe],
        ingredients: dict[str, Ingredient],
        inventory: Inventory):
    while True:
        choice = input("Выберите вариант: ")
        if choice == "0":
            return create_custom_recipe(inventory)
        else:
            return recipes[int(choice)]

def choose_payment():
    print("Выберите способ оплаты: ")
    print("1 - Наличные")
    print("2 - Карта")

    while True:
        choice = input("Выберите: ")

        if choice == "1":
            return CashPayment(), "Наличные"
        elif choice == "2":
            return CardPayment(), "Карта"
        
        print("Выберите между 1 и 2 вариантами")

def create_order(
        ingredients: dict[str, Ingredient],
        inventory: Inventory,
        report: SalesReport,
        file_saver: FileOrderSaver):
    recipes = RecipeFactory.get_standard_recipes()
    items: list[OrderItem] = []

    while True:
        show_standard_recipes(recipes, ingredients)

        recipe = choose_recipe(recipes, ingredients, inventory)
        quantity = int(input("Введите количество: "))

        if not inventory.has_enough(recipe.ingredient_keys, quantity):
            print("Недостаточно ингредиентов для заказа.")
            return
        
        items.append(OrderItem(recipe, quantity))

        more = input("Добавить ещё один вид пиццы?")

        if more == "нет":
            break

    payment_strategy, payment_type = choose_payment()
    order = Order(items, payment_type)

    for item in items:
        inventory.reduce_stock(item.recipe.ingredient_keys, item.quantity)

    # Сумма заказа
    amount = order.total_price(ingredients)

    # Оплата
    print(payment_strategy.pay(amount))

    # Сохранение заказа в файл
    file_saver.save(order, ingredients)

    # Добавление заказа в отчёт
    report.add_order(order, ingredients)

def main():
    ingredients = create_ingredients()
    stock = create_stock()

    inventory = Inventory(ingredients, stock)
    report = SalesReport()
    file_saver = FileOrderSaver()

    while True:
        show_menu()

        choice = input("Выберите пункт меню")
        if choice == "1":
            create_order(ingredients, inventory, report, file_saver)
        elif choice == "2":
            report.show()
        elif choice == "3":
            inventory.show()
        elif choice == "4":
            break

main()