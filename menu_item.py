"""
File Name: menu_item.py
Author: Ntyam Adjomo Francky Ludovic

Purpose: create a program that stores a list of products in a shopping cart along with their prices. 
         The user should have the ability to add items to the list, remove them, and see the total price of the cart.

This program also contains a way to Showing Creativity and Exceeding Requirements.
"""
print("------------------- Final Requirements -----------------\n")
print("Welcome to the Shopping Cart Program!\n")

#Variable that will contain the list of  items name and price.
list_of_name = []
list_of_price = []

action = 0

while action != 5 :
     print("")
     print("Please select one of the following:\n1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit")
     action = int(input("Please enter an action: "))

     if action == 1 :
         name_item = input("What item would you like to add? ")
         list_of_name.append(name_item.capitalize())
         price_item = float(input(f"What is the price of '{name_item}'? "))
         list_of_price.append(price_item)
         print(f"'{name_item}' has been added to the cart.\n")

     elif action == 2 :
         print("The contents of the shopping cart are:")
         for index in range(len(list_of_name)):
             print(f"{index + 1}. {list_of_name[index]:10}  ${list_of_price[index]:.2f}")

             
     elif action == 3 :
         remove_item = int(input("Which item would you like to remove? "))
         if remove_item - 1 >= len(list_of_price) :
             print("Sorry, that is not a valid item number.")
         else:
             list_of_name.pop(remove_item - 1) 
             list_of_price.pop(remove_item - 1)   
             print("Item removed.")  

     elif action == 4 :
         total_price = 0
         for price in list_of_price :
             total_price += price           
         print(f"The total price of the items in the shopping cart is ${total_price:.2f}")

     elif action == 5 :
          print("Thank you. Goodbye.")

