from customer import Customer
from coffee import Coffee
from order import Order

# Session memory
session_customers = {}         
customer_visits = {}           
session_coffees = {}          

print("Welcome to the Coffee Shop Terminal")

while True:
    # Get and clean customer name
    raw_name = input("\nEnter customer name: ")
    name = raw_name.strip().lower()

    # Handle customer
    if name in session_customers:
        customer = session_customers[name]
        customer_visits[name] += 1
        print(f"{customer.name} is a repeat customer ({customer_visits[name]} times).")
    else:
        customer = Customer(name)
        session_customers[name] = customer
        customer_visits[name] = 1
        print(f"{customer.name} is a new customer - make them feel welcome!")

    # Handle coffee
    coffee_name = input("Enter coffee name: ").strip()

    if coffee_name in session_coffees:
        coffee = session_coffees[coffee_name]
        print(f"{coffee.name} has been ordered {coffee.num_orders()} times.")
    else:
        coffee = Coffee(coffee_name)
        session_coffees[coffee_name] = coffee
        print(f"{coffee.name} is a new coffee - adding to menu.")

    # Get price
    try:
        price = float(input("Enter price in KSH: "))

        # Check for discount
        current_aficionado = Customer.most_aficionado(coffee)
        if current_aficionado and current_aficionado == customer:
            print("You're our most aficionado for this coffee! You get a 10% discount.")
            price *= 0.9

        # Create order
        order = Order(customer, coffee, price)

        print("\nOrder placed successfully!")
        print(f"Customer: {customer.name}")
        print(f"Coffee: {coffee.name}")
        print(f"Price: KSH {order.price:.2f}")

    except ValueError:
        print("Invalid price. Please enter a number.")
        continue  # Retry input

    # Ask if barista wants to place another order or end session
    next_action = input("\nWould you like to place another order? (yes/no): ").strip().lower()
    if next_action not in ["yes", "y"]:
        print("Ending session. Have a great day at the Coffee Shop!")
        break
