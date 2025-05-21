from customer import Customer
from coffee import Coffee

def main():
    customers = []
    coffees = []
    print("Welcome to the Coffee Shop CLI!")

    while True:
        print("\nMenu:")
        print("1. Add Customer")
        print("2. Add Coffee")
        print("3. Place Order")
        print("4. List Customers")
        print("5. List Coffees")
        print("6. Show Coffee Stats")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            name = input("Enter customer name (1-15 chars): ")
            try:
                customer = Customer(name)
                customers.append(customer)
                print(f"Added customer: {customer}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            name = input("Enter coffee name (at least 3 chars): ")
            try:
                coffee = Coffee(name)
                coffees.append(coffee)
                print(f"Added coffee: {coffee}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            if not customers or not coffees:
                print("Add customers and coffees first!")
                continue
            print("Customers:")
            for i, c in enumerate(customers):
                print(f"{i + 1}. {c.name}")
            c_index = int(input("Select customer number: ")) - 1

            print("Coffees:")
            for i, c in enumerate(coffees):
                print(f"{i + 1}. {c.name}")
            coffee_index = int(input("Select coffee number: ")) - 1

            price = input("Enter price in KSH (130.0 - 1300.0): ")
            try:
                price = float(price)
                order = customers[c_index].create_order(coffees[coffee_index], price)
                print(f"Order placed: {order}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Customers:")
            for customer in customers:
                print(f"{customer}")

        elif choice == "5":
            print("Coffees:")
            for coffee in coffees:
                print(f"{coffee}")

        elif choice == "6":
            print("Coffees Stats:")
            for coffee in coffees:
                print(f"{coffee}: Orders = {coffee.num_orders()}, Avg Price = {coffee.average_price():.2f} KSH")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please pick a number between 1 and 7.")

if __name__ == "__main__":
    main()
