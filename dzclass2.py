class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def describe_device(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price} USD")


class CoffeeMachine(Device):
    def __init__(self, brand, model, price, water_tank_capacity):
        super().__init__(brand, model, price)
        self.water_tank_capacity = water_tank_capacity

    def describe_device(self):
        super().describe_device()
        print(f"Water Tank Capacity: {self.water_tank_capacity} L")


class Blender(Device):
    def __init__(self, brand, model, price, speed_settings):
        super().__init__(brand, model, price)
        self.speed_settings = speed_settings

    def describe_device(self):
        super().describe_device()
        print(f"Speed Settings: {self.speed_settings}")


class MeatGrinder(Device):
    def __init__(self, brand, model, price, material):
        super().__init__(brand, model, price)
        self.material = material

    def describe_device(self):
        super().describe_device()
        print(f"Material: {self.material}")


coffee_machine = CoffeeMachine("DeLonghi", "EC155", 150, 1.1)
coffee_machine.describe_device()
print("\n")

blender = Blender("Philips", "HR3652", 200, 5)
blender.describe_device()
print("\n")

meat_grinder = MeatGrinder("Bosch", "MFW67440", 250, "Stainless Steel")
meat_grinder.describe_device()
print("\n")


class Money:
    def __init__(self, dollars, penny):
        self.dollars = dollars
        self.penny = penny
        self.normalize()

    def normalize(self):
        if self.penny >= 100:
            self.dollars += self.penny // 100
            self.penny = self.penny % 100
        elif self.penny < 0:
            self.dollars += self.penny // 100
            self.penny = 100 + self.penny % 100

    def display(self):
        print(f"{self.dollars} dollars and {self.penny} cents")

    def set_dollars(self, dollars):
        self.dollars = dollars
        self.normalize()

    def set_penny(self, penny):
        self.penny = penny
        self.normalize()


class Product:
    def __init__(self, name, price_dollars, price_penny):
        self.name = name
        self.price = Money(price_dollars, price_penny)

    def display(self):
        print(f"Product: {self.name}")
        self.price.display()

    def reduce_price(self, reduction_dollars, reduction_penny):
        total_cents = self.price.dollars * 100 + self.price.penny
        reduction_cents = reduction_dollars * 100 + reduction_penny
        new_total_cents = total_cents - reduction_cents
        self.price.dollars = new_total_cents // 100
        self.price.penny = new_total_cents % 100
        self.price.normalize()


wallet = Money(10, 125)
wallet.display()
wallet.set_dollars(11)
wallet.set_penny(250)
wallet.display()

product = Product("Chips", 5, 25)
product.display()
product.reduce_price(2, 30)
product.display()


class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.price < other.price

    def __le__(self, other):
        return self.price <= other.price

    def __gt__(self, other):
        return self.price > other.price

    def __ge__(self, other):
        return self.price >= other.price
