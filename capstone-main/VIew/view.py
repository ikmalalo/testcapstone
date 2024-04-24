from prettytable import PrettyTable
from colorama import Fore

def display_menu_and_stock(laptops):
   table = PrettyTable(["Laptop", "Price", "Stock"])
   for laptop in laptops:
      table.add_row([Fore.BLUE + laptop['name'], Fore.BLUE + str(laptop['price']), Fore.BLUE + str(laptop['stock'])])
   print(Fore.BLUE + "Laptop Shop Menu and Stock")
   print(table)

def display_order_history(self):
      table = PrettyTable()
      table.field_names = ["Customer Name", "Laptop Name", "Quantity", "Price"]
      for order in self.order_queue:
         customer_name, laptop_name, quantity = order
         price = next((laptop["price"] for laptop in self.laptops if laptop["name"].lower() == laptop_name.lower()), None)
         if price is not None:
            table.add_row([customer_name, laptop_name.capitalize(), quantity, price])
         else:
            table.add_row([customer_name, laptop_name.capitalize(), quantity, "Price not found"])  
      return table