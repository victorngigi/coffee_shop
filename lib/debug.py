from customer import Customer
from coffee import Coffee
from order import Order

if __name__ == "__main__":
    # Reset any existing orders
    Order.all.clear()

    # Demo customers, coffees, and orders
    c1 = Customer("Alice")
    c2 = Customer("Bob")

    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")

    o1 = c1.create_order(coffee1, 450.0)
    o2 = c1.create_order(coffee1, 500.0)
    o3 = c2.create_order(coffee1, 600.0)
    o4 = c2.create_order(coffee2, 300.0)

    # Print using __repr__ for readability
    print("Customers who ordered Latte:", coffee1.customers())
    print("Average price of Latte: {:.2f} KSH".format(coffee1.average_price()))

    top = Customer.most_aficionado(coffee1)
    if top:
        print("Customer who spent most on Latte:", top.name)
    else:
        print("No orders for Latte yet.")
