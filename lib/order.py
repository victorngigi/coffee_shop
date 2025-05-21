class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(price, float):
            raise ValueError("Price must be a float")
        if not (130.0 <= price <= 1300.0):
            raise ValueError("Price must be between 130 and 1300 KSH")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
    
    def __repr__(self):
        return f"Order({self._customer}, {self._coffee}, {self._price})"
