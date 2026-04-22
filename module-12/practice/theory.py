# Singleton

class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.mode = "prod"
        return cls._instance


# Factory Method

class EmailSender:
    def send(self, message):
        return f"Email: {message}"
    
class SmsSender:
    def send(self, message):
        return f"SMS: {message}"
    
class NotificationFactory:
    @staticmethod
    def create(channel):
        if channel == "email":
            return EmailSender()
        if channel == "sms":
            return SmsSender()
        raise ValueError("Unknown channel")
    
sender = NotificationFactory.create("sms")
sender.send("Ваш код подтверждения 1234")


# Abstract Factory

class LightButton:
    def render(self):
        return "LightButton"
    
class LightInput:
    def render(self):
        return "LightInput"

class DarkButton:
    def render(self):
        return "DarkButton"

class DarkInput:
    def render(self):
        return "DarkInput"
    
class LightThemeFactory:
    def create_button(self):
        return LightButton
    
    def create_input(self):
        return LightInput
    
class DarkThemeFactory:
    def create_button(self):
        return DarkButton
    
    def create_input(self):
        return DarkInput
    
def build_form(factory):
    button = factory.create_button()
    field = factory.create_field()
    print(button.render(), field.render())

build_form(LightThemeFactory())


# Builder

class LaptopBuilder:
    def __init__(self):
        self.laptop = {
            "cpu": "intel i5",
            "ram": 8,
            "ssd": 256,
            "gru": "Intergrated"
        }

    def for_study(self):
        self.laptop["ram"] = 16
        self.laptop["ssd"] = 512
        return self

    def for_gaming(self):
        self.laptop["ram"] = 32
        self.laptop["ssd"] = 1024
        self.laptop["gru"] = "RTX 4070"
        return self
    
    def with_cpu(self, cpu):
        self.laptop["cpu"] = cpu
        return self
    
    def build(self):
        return self.laptop.copy()
    
print(LaptopBuilder().for_study().with_cpu("Intel i7").build)


# Prototype

import copy

template_order = {
    "delivery": "standard",
    "promo": False,
    "items": ["book"]
}

fast_order = copy.deepcopy(template_order)
fast_order["delivery"] = "express"

print(template_order, fast_order)


# Структурные паттерны
# Adapter

class OldSmsService:
    def send_sms(self, phone, text):
        print(f"old_service: {phone} : {text}")

class SmsAdapter:
    def __init__(self, service, phone):
        self.service = service
        self.phone = phone

    def send(self, message):
        self.service.send_sms(self.phone, message)

SmsAdapter(OldSmsService(), "+79999999999").send("Сообщение")


# Структурные паттерны
# Bring

class TV:
    def turn_on(self):
        return "TV is on"
    
class Radio:
    def turn_on(self):
        return "Radio is on"
    
class RemoveControl:
    def __init__(self, device):
        self.device = device

    def power(self):
        return self.device.turn_on()
    
print(RemoveControl(TV()).power())


# Структурные паттерны
# Composite

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def get_size(self):
        return self.size
    
class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, child):
        self.children.append(child)

    def get_size(self):
        return sum(child.get_size() for child in self.children)
    
docs = Folder("docs")
docs.add(File("text_1.txt", 10))
docs.add(File("text_2.txt", 20))

print(docs.get_size())


# Структурные паттерны
# Decorator

class Coffee:
    def price(self):
        return 120
    
    def description(self):
        return "Кофе"
    
class MilkDecorator:
    def __init__(self, drink):
        self.drink = drink

    def price(self):
        return self.drink.price() + 30
    
    def description(self):
        return self.drink.description() + ", молоко"

class SypupDecorator:
    def __init__(self, drink):
        self.drink = drink

    def price(self):
        return self.drink.price() + 25
    
    def description(self):
        return self.drink.description() + ", сироп"
    
drink = SypupDecorator(MilkDecorator(Coffee()))
print(drink.price(), drink.description())


# Структурные паттерны
# Facade

class PaymentService:
    def pay(self, amount):
        print(f"Оплата {amount} подтверждена")

class WarehouseService:
    def pay(self, item):
        print(f"Товар {item} зарезервирован")

class DeliveryService:
    def pay(self, item):
        print(f"Доставка для {item} создана")

class OrderFacade:
    def __init__(self):
        self.payment = PaymentService()
        self.warehouse = WarehouseService()
        self.delivery = DeliveryService()

    def place_order(self, item, amount):
        self.payment.pay(amount)
        self.warehouse.reserve(item)
        self.delivery.create(item)
        print("Заказ оформлен")

OrderFacade().place_order("Наушники", 9999)


# Структурные паттерны
# FlyWeight

class Flyweight:
    def __init__(self, color):
        self.color = color

    def draw(self, x, y):
        print(self.color, x, y)

class Factory:
    # _cached == {}?

    @classmethod
    def get(cls, color):
        if color not in cls._cached:
            cls._cached[color] = Flyweight(color)
        return cls._cached(color)
    
red1 = Factory.get("red")
red2 = Factory.get("red")

print(red1 is red2) = True


# Структурные паттерны
# Proxy

class Image:
    def __init__(self, path):
        print("Загрузка")
        self.path = path

    def show(self):
        print(f"Show {self.path}")

class ImageProxy:
    def __init__(self, path):
        self.path = path
        self._real = None

    def show(self):
        if self._real is None:
            self._real = Image(self.path)

        self._real.show()

Img = Image("photo.png")
Img.show() # Загрузка
Img.show() # Пусто


# Поведенческие паттерны
# Chain of Responsibility

class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return "Unhandled"

class AuthHandler(Handler):
    def handle(self, request):
        if not request.get("user"):
            return "401 Unathorized"
        return super().handle(request)
    
class RoleHandler(Handler):
    def handle(self, request):
        if request.get("role") != "admin":
            return "403 Forbidden"
        return super().handle(request)
    
chain = AuthHandler(RoleHandler())
print(chain.handle({"user": "alice", "role": "admin"}))


# Поведенческие паттерны
# Command

class Light:
    def on(self):
        print("Light is on")

class TurnOnCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()
    
class Button:
    def __init__(self, command):
        self.command = command

    def press(self):
        self.command.execute()

Button(TurnOnCommand(Light())).press()


# Поведенческие паттерны
# Mediator

class ChatMediator:
    def send(self, message, user):
        for c in user.colleagues:
            if c is not user:
                c.receive(message)

class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator - mediator
        self.colleagues = []

    def send(self, message):
        self.mediator.send(f"{self.name}: {message}", self)

    def receive(self, message):
        print(message)

mediator = ChatMediator()
alice = User("Alice", mediator)
bob = User("Bob", mediator)
alice.colleagues = [alice, bob]
bob.colleagues = [alice, bob]
alice.send("Привет")


# Поведенческие паттерны
# Memento

class Editor:
    def __init__(self):
        self.text = ""

    def write(self, text):
        self.text += text

    def save(self):
        return self.text
    
    def restore(self, snapshot):
        self.text = snapshot

editor = Editor()
editor.write("Hello")
snapshot = editor.save
editor.write(", world")
print(editor.text) # Hello, world
editor.restore(snapshot)
print(editor.text) # World


# Поведенческие паттерны
# Observer

class Order:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, listener):
        self.subscribers.append(listener)

    def set_status(self, status):
        for subscriber in self.subscribers:
            subscriber(status)

def email_listener(status):
    print(f"Email: Произошла смена статуса на {status}")

def sms_listener(status):
    print(f"SMS: Произошла смена статуса на {status}")

order = Order()
order.subscribe(email_listener)
order.subscribe(sms_listener)
order.set_status("delivery")


# Поведенческие паттерны
# State

class DraftState:
    def publish(self, document):
        document.state = ReviewState()
        return "Черновик отправлен на проверку"
    
class ReviewState:
    def publish(self, document):
        document.state = PublishedState()
        return "Документ опубликован"
    
class PublishedState:
    def publish(self, document):
        return "Уже опубликован"
    
class Document:
    def __init__(self):
        self.status = DraftState()

    def publish(self):
        return self.state.publish(self)
    
doc = Document()
doc.publish() # Черновик отправлен на проверку
doc.publish() # Документ опубликован
doc.publish() # Уже опубликован


# Поведенческие паттерны
# Strategy

class StandardDelivery:
    def calculate(self, weight):
        return 200 + weight * 10
    
class ExpressDelivery:
    def calculate(self, weight):
        return 500 + weight * 20
    
class PickupDelivery:
    def calculate(self, weight):
        return 0
    
class DeliveryCalc:
    def __init__(self, strategy):
        self.strategy = strategy

    def get_price(self, weight):
        return self.strategy.calculate(weight)
    
print(DeliveryCalc(PickupDelivery()).get_price(10))


# Поведенческие паттерны
# Template Method

class ReportTemplate:
    def build(self):
        data = self.fetch_data()
        return self.format_data(data)
    
    def fetch_data(self):
        raise NotImplementedError
    
    def format_data(self, data):
        raise NotImplementedError
    
class SalesReport(ReportTemplate):
    def fetch_data(self):
        return [100, 200, 300]
    
    def format_data(self, data):
        return f"Сумма продаж: {sum(data)}"
    
print(SalesReport().build())


# Поведенческие паттерны
# Visitor

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        return visitor.visit_book(self)
    
class Course:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def accept(self, visitor):
        return visitor.visit_book(self)
    
class DiscountVisitor:
    def visit_book(self, book):
        return f"{book.title}: {book.price * 0.9}"
    
    def visit_course(self, course):
        return f"{course.title}: {course.price * 0.2}"
    
visitor = DiscountVisitor
items = [Book("book", 1000), Course("course", 5000)]
for item in items:
    print(item.accept(visitor))