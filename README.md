# **Coffee Shop Domain Model**

This is a Python application modeling a Coffee Shop domain using Object-Oriented Programming.
The domain includes Customer, Coffee, and Order classes with relationships and business logic implemented.

## Features

* Create Customers and Coffees
* Customers can place Orders for Coffees with prices in KSH
* Retrieve Orders by Customer or Coffee
* Calculate average coffee price and find top customer (most aficionado)
* Interactive terminal-based interface to place orders and query data

## Setup

1. Clone or download this repository
2. (Optional but recommended) Set up a virtual environment:
   <code>
   python -m venv venv
   source venv/bin/activate   #(On Windows: venv\Scripts\activate)
   </code>
4. Install dependencies (if any):
   <code>
   pip install -r requirements.txt
   #(Currently, no external dependencies needed)
   </code>

## Running the Application
Run the interactive Coffee Shop program:
<code>
python main.py
</code>
You will see a menu with options to:

* Create Customers and Coffees
* Place Orders
* View Orders and Customer/Coffee summaries
* Exit the program
  Follow on-screen prompts to interact with the Coffee Shop.

## Project Structure
coffee _shop/
customer.py          # Customer class
coffee.py            # Coffee class
order.py             # Order class
main.py              # Interactive CLI application
testing/               # Unit tests

## Testing
run:
<code>
pytest
</code>

## Notes

* Customer names must be 1–15 characters long.
* Coffee names must be at least 3 characters long.
* Order prices must be between 130 and 1300 KSH.


