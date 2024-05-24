class Car:
    def __init__(self, model_name, year, manufacturer, engine, color, price):
        self.model_name = model_name
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    def describe_car(self):
        print(f"Model Name: {self.model_name}")
        print(f"Year: {self.year}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine : {self.engine} L")
        print(f"Car Color: {self.color}")
        print(f"Price: {self.price} USD")

    def update_price(self, new_price):
        self.price = new_price
        print(f"New price set: {self.price} USD")

    def update_color(self, new_color):
        self.color = new_color
        print(f"New car color: {self.color}")


car = Car(
    model_name="Audi RS6",
    year="2022",
    manufacturer="VAG",
    engine="4",
    color="Black",
    price="130000"
)
car.describe_car()

car.update_price(100000)

car.update_color("Red")
print("\n")

car.describe_car()


class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def describe_book(self):
        print(f"Title: {self.title}")
        print(f"Year of Publication: {self.year}")
        print(f"Publisher: {self.publisher}")
        print(f"Genre: {self.genre}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price} USD")

    def update_price(self, new_price):
        self.price = new_price
        print(f"New price set: {self.price} USD")

    def update_genre(self, new_genre):
        self.genre = new_genre
        print(f"New book genre: {self.genre}")


# Example usage
book = Book(
    title="The Lord of the Rings",
    year=1954,
    publisher="Allen & Unwin",
    genre="Fantasy",
    author="J.R.R. Tolkien",
    price="15"
)
book.describe_book()

book.update_price(25)

book.update_genre("Epic Fantasy")
print("\n")

book.describe_book()


class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def describe_stadium(self):
        print(f"Name: {self.name}")
        print(f"Opening Date: {self.opening_date}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity}")

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity
        print(f"New capacity set: {self.capacity}")

    def update_name(self, new_name):
        self.name = new_name
        print(f"New name: {self.name}")


stadium = Stadium(
    name="Olimpiyskiy National Sports Complex",
    opening_date="1923",
    country="Ukraine",
    city="Kyiv",
    capacity=70050
)
stadium.describe_stadium()

stadium.update_capacity(72050)

stadium.update_name("NSC Olimpiyskiy")
print("\n")

stadium.describe_stadium()
