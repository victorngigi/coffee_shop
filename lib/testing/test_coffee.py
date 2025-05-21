import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("A")
    coffee = Coffee("Cappuccino")
    assert coffee.name == "Cappuccino"

def test_coffee_orders_and_customers():
    Order.all.clear()
    coffee = Coffee("Americano")
    alice = Customer("Alice")
    bob = Customer("Bob")
    alice.create_order(coffee, 150.0)
    bob.create_order(coffee, 200.0)

    assert len(coffee.orders()) == 2
    customers = coffee.customers()
    assert alice in customers
    assert bob in customers

def test_coffee_num_orders_and_avg_price():
    Order.all.clear()
    coffee = Coffee("Mocha")
    customer = Customer("John")
    customer.create_order(coffee, 130.0)
    customer.create_order(coffee, 230.0)
    assert coffee.num_orders() == 2
    assert coffee.average_price() == 180.0
