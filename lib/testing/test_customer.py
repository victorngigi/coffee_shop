import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_customer_orders_and_coffees():
    customer = Customer("Bob")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 200.0)
    customer.create_order(coffee2, 300.0)

    assert len(customer.orders()) == 2
    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()

def test_customer_most_aficionado():
    Order.all.clear()
    alice = Customer("Alice")
    bob = Customer("Bob")
    latte = Coffee("Latte")
    alice.create_order(latte, 400.0)
    alice.create_order(latte, 500.0)
    bob.create_order(latte, 600.0)
    assert Customer.most_aficionado(latte) == alice
