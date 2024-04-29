from statistics import mean


class Coffee:
    def __init__(self, name):
        self.name = name

    def orders(self):
        # return all orders with list comprehension
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        # return non-duplicate list via set
        return list({order.customer for order in Order.all if order.coffee is self})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        # return all order prices with list comprehension
        prices = [order.price for order in Order.all if order.coffee is self]
        return mean(prices)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not hasattr(self, "_name"):
            self._name = name
        # else:
        #     raise Exception("Coffee name can't be changed")


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    def orders(self):
        # return all orders with list comprehension
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        # return non-duplicate list via set
        return list({order.coffee for order in Order.all if order.customer is self})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    def spent_on(self, coffee):
        prices = [
            order.price
            for order in Order.all
            if order.customer is self and order.coffee is coffee
        ]
        return sum(prices)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and (0 < len(name) <= 15):
            self._name = name

    @classmethod
    def most_aficionado(cls, coffee):
        return max(cls.all, key=lambda customer: customer.spent_on(coffee))


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.__class__.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if (
            not hasattr(self, "_price")
            and isinstance(price, float)
            and (1.0 <= price <= 10.0)
        ):
            self._price = price
