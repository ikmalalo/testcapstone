from collections import deque
from colorama import init, Fore

class User:
   def __init__(self, username, password):
      self.username = username
      self.password = password

class Admin(User):
   def __init__(self, username, password):
      super().__init__(username, password)

   def delete_order(self, shop, customer_name):
      shop.delete_order(customer_name)




class Customer(User):
   def __init__(self, username, password):
      super().__init__(username, password)

   def place_order(self, laptop_name, quantity, shop):
      laptop_name = laptop_name.lower()
      for laptop in shop.laptops:
         if laptop['name'].lower() == laptop_name:
            if laptop['stock'] >= quantity:
                  order = (self.username, laptop_name, quantity)
                  shop.order_queue.append(order)
                  laptop['stock'] -= quantity
                  print(Fore.GREEN + f"Order placed by {self.username}: {quantity} {laptop_name.capitalize()}(s)")
            else:
                  raise ValueError(f"Insufficient stock for {laptop_name.capitalize()}") 
            return
      raise ValueError(f"Laptop '{laptop_name.capitalize()}' not found") 


class LaptopShop:
   _instance = None

   def __new__(cls):
      if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Inisialisasi atribut atau lakukan hal lain yang diperlukan
            cls._instance.laptops = [
               {"name": "Laptop A", "price": 10000000, "stock": 10},
               {"name": "Laptop B", "price": 8000000, "stock": 5},
               {"name": "Laptop C", "price": 6000000, "stock": 8}
            ]
            cls._instance.total_income = 0
            cls._instance.order_stack = deque()
            cls._instance.order_queue = deque()
            cls._instance.menu = []
            cls._instance.orders = []
      return cls._instance

   def calculate_total_income(self):
      return self.total_income
   
   def update_laptop(self, laptop_name, new_price, new_stock):
      laptop_found = False
      for laptop in self.laptops:
         if laptop['name'].lower() == laptop_name.lower():
               laptop['price'] = new_price
               laptop['stock'] = new_stock
               laptop_found = True
               print(f"Laptop '{laptop_name}' updated successfully.")
               break
      
      if not laptop_found:
         print(f"Laptop '{laptop_name}' not found.")

   def add_new_laptop(self, laptop_name, price, stock, location):
      if location not in ['beginning', 'middle', 'end']:
         raise ValueError("Invalid location. Please choose 'beginning', 'middle', or 'end'.")

      if location == 'beginning':
         self.laptops.insert(0, {"name": laptop_name, "price": price, "stock": stock})
      elif location == 'end':
         self.laptops.append({"name": laptop_name, "price": price, "stock": stock})
      elif location == 'middle':
         middle_index = len(self.laptops) // 2
         self.laptops.insert(middle_index, {"name": laptop_name, "price": price, "stock": stock})

   def del_laptop(self, location=None):
      if location not in ['beginning', 'middle', 'end']:
         raise ValueError("Invalid location. Please choose 'beginning', 'middle', or 'end'.")

      if location == 'beginning':
         if self.laptops:
               deleted_laptop = self.laptops.pop(0)
         else:
               raise ValueError("No laptops found to delete.")
      elif location == 'end':
         if self.laptops:
               deleted_laptop = self.laptops.pop()
         else:
               raise ValueError("No laptops found to delete.")
      elif location == 'middle':
         if not self.laptops:
               raise ValueError("No laptops found to delete.")

         if len(self.laptops) == 1:
               raise ValueError("There is only one laptop available. You cannot delete it from the middle.")

         laptop_to_delete = input("Enter the laptop name to delete: ")
         for laptop in self.laptops:
               if laptop['name'] == laptop_to_delete:
                  self.laptops.remove(laptop)
                  return
         raise ValueError(f"Laptop '{laptop_to_delete}' not found.")
      
   def display_order_history(self):
      return self.latops

   def display_menu_and_stock(self):
      return self.laptops

   def update_menu_and_stock(self):
      return self.laptops

   def display_orders(self):
      return self.order_queue

   def sort_menu_by_price(self):
      return sorted(self.laptops, key=lambda x: x['price'])

   def sort_menu_by_stock(self):
      return sorted(self.laptops, key=lambda x: x['stock'])

   def search_menu(self, keyword):
      results = []
      for laptop in self.laptops:
         for key, value in laptop.items():
               if keyword.lower() in str(value).lower():
                  results.append(laptop)
                  break  
      return results
