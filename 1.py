from __future__ import annotations
from abc import ABC, abstractmethod


# начало реализую через фабрики, но при этом в самих пиццах будет только название и цена, так как я не знаю, как это все реализовать иначе
class Creating(ABC):
    def create_pizza(self):
        pass


class PizzaPizzeta(Creating):
    def create_pizza(self):
        return Pizzeta()


class PizzaMinni(Creating):
    def create_pizza(self):
        return Minni()


class PizzaHome(Creating):
    def create_pizza(self):
        return Home()


class PizzaGentle(Creating):
    def create_pizza(self):
        return Gentle()


class PizzaByMyself(Creating):
    def create_pizza(self):
        return Myself()


class Pizza(ABC):
    def __init__(self, toppings):
        self.toppings = toppings

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Pizzeta(Pizza):
    def get_name(self):
        return "Pizzeta"

    def get_price(self):
        return 520


class Minni(Pizza):
    def get_name(self):
        return "Minni"

    def get_price(self):
        return 240


class Home(Pizza):
    def get_name(self):
        return "Home"

    def get_price(self):
        return 360


class Gentle(Pizza):
    def get_name(self):
        return "Gentle"

    def get_price(self):
        return 400


class Myself(Pizza):
    def get_name(self):
        return self.name

    def get_price(self):
        return 600


class PizzaShop:
    def __init__(self):
        self.orders = []  # заказы
        self.revenue = 0  # доход
        # self.pizza_factory = ???()

    def order_pizza(self, pizza_type, toppings):
        pizza = self.pizza_factory.create_pizza(pizza_type, toppings)
        self.orders.append(pizza)
        self.revenue += pizza.get_price()
        return pizza

    def get_sales_report(self) -> None:
        print(f"итоговый доход: {self.revenue} рублей")

# рассчет прибыли и сохранение не получились(

# один вопрос есть, из-за которого этот код нерабочий. Что я должна вызывать на 80-й строке?? если бы я делала фабрику через if, то тогда все бы было понятно, но так как вы говорите, что через if неверно, тогда я вообще не знаю
#отдельные классы топпингам и ингридиентам я тоже не придумала, так как тогда вообще странный код выходит