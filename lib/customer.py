from order import Order

class Customer:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 characters long")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    @classmethod
    def baller_customer(cls, coffee):
        customer_spending = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customer_spending:
                    customer_spending[order.customer] = 0
                customer_spending[order.customer] += order.price

        if not customer_spending:
            return None

        return max(customer_spending, key=customer_spending.get)
