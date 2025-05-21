import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization_and_validation():
    Order.all.clear()
    customer = Customer("David")
    coffee = Coffee("Macchiato")

    with pytest.raises(ValueError):
        Order(customer, coffee, "free")
    with pytest.raises(ValueError):
        Order(customer, coffee, 129.0)
    with pytest.raises(ValueError):
        Order(customer, coffee, 1301.0)

    order = Order(customer, coffee, 250.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 250.0
