from order import Order

class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 characters")
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __repr__(self):
        return f"Customer({self._name})"

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        customer_totals = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer not in customer_totals:
                    customer_totals[order.customer] = 0
                customer_totals[order.customer] += order.price

        if not customer_totals:
            return None

        return max(customer_totals, key=customer_totals.get)
