"""
File Name: shopping_list.py
Author: Ntyam Adjomo Francky Ludovic
Purpose: Ask the user for a list of list of items in a shopping list, stop asking for items when the user types "quit."
"""
# variable contain empty list.
shopping_list =[]
print("Please enter the items of the shopping list (type: quit to finish):")

items = ""
while items.lower() != "quit" :
      items = input("Item: ")
      if items.lower() != "quit":
           shopping_list.append(items)
print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

print("\nThe shopping list with indexes is:")
for index in range(len(shopping_list)):
    print(f"{index}. {shopping_list[index]}")

index_item = int(input("\nWhich item would you like to change? "))
new_item  = input("What is the new item? ")
shopping_list[index_item] = new_item

print("\nThe shopping list with indexes is:")
for index in range(len(shopping_list)):
    print(f"{index}. {shopping_list[index]}")