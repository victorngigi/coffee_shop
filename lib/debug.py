from customer import Customer
from coffee import Coffee
from order import Order

# Demo customers, coffees, and orders
c1 = Customer("Alice")
c2 = Customer("Bob")

coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

o1 = c1.create_order(coffee1, 450.0)
o2 = c1.create_order(coffee1, 500.0)
o3 = c2.create_order(coffee1, 600.0)
o4 = c2.create_order(coffee2, 300.0)

print("Customers who ordered Latte:", [customer.name for customer in coffee1.customers()])
print("Average price of Latte:", coffee1.average_price())
print("Customer who spent most on Latte:", Customer.most_aficionado(coffee1).name)  
