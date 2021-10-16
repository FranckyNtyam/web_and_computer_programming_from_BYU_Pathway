"""
File: milestone03.py
Author: Brother Francky Ntyam

Purpose: 03 Prove: Milestone - Meal Price Calculator.

This program also contains a way to Showing Creativity and Exceeding Requirements.
"""
# variable contain the price of a child's meal.

child_meal = float(input("What is the price of a child's meal? "))

# variable contain the price of an adult's meal.

adult_meal = float(input("What is the price of an adult's meal? "))

# variable contain the number of children.

number_of_child = int(input("How many children are there? "))

# variable contain the number of adults.

number_of_adult = int(input("How many adults are there? "))

# variable contain the sales tax rate.

sales_tax_rate = float(input("What is the sales tax rate? "))

print("")

# variable contain the subtotal without sale tax.

subtotal = (child_meal * number_of_child) + (adult_meal * number_of_adult)

# display subtotal

print(f"Subtotal: {subtotal}")

#Showing Creativity and Exceeding Requirements.
print("---------------------------------------")
print("Showing Creativity and Exceeding Requirements.\n")
#variables with the list of child and adult meal
child_meal_list = ["Milk", "Candy", "Biscuit","Chocolate", "juice"]
adult_meal_list = ["Burger", "appetizers", "drink", "salad"]

type_of_meal = str(input("What type of meal you want? child or adult? "))
if type_of_meal == "child":
    print("\nDo your choice of child's meal in list below:")
    for i in range(len(child_meal_list)):
        print(f"{i} {child_meal_list[i]}")
    child_meal_choice = int(input("Enter the number of child's meal you want? "))
    child_meal_price = float(input(f"What is the price of {child_meal_list[child_meal_choice]} ? "))
    number_of_child = int(input("How many children want it? "))
    sales_tax_rate = float(input("What is the sales tax rate? "))
    subtotal = (child_meal_price * number_of_child)
    print(f"Subtotal: {subtotal}")  
elif type_of_meal == "adult":
    print("Do your choice of adult's meal in list below:")
    for i in range(len(adult_meal_list)):
        print(f"{i} {adult_meal_list[i]}")
    adult_meal_choice = int(input("Enter the number of adult's meal you want? "))
    adult_meal_price = float(input(f"What is the price of {adult_meal_list[adult_meal_choice]}? "))
    number_of_adult = int(input("How many adults want it? "))
    sales_tax_rate = float(input("What is the sales tax rate? "))
    subtotal = (adult_meal_price * number_of_adult)
    print(f"Subtotal: {subtotal}")
else:
    print("Restart the program")





