from customer import Customer
from coffee import Coffee
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of Customer")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of Coffee")
        self._coffee = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int)):
            raise ValueError("Price must be a whole number, no decimals")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
