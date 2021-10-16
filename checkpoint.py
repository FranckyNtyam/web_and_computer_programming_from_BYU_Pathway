"""
File: checkpoint.py
Author: Brother Francky Ntyam

Purpose: 05 Prepare: Checkpoint.
"Practicing If statments"

This program also contains a way to Showing Creativity and Exceeding Requirements.
"""
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))

if number_one > number_two:
    print("The first number is greater")
else:
    print("The first number is not greater")

if number_one == number_two:
    print("The numbers are equal")
else:
    print("The number are not equal")

if number_two > number_one:
    print("The second number is greater")
else:
    print("The second number is not greater")

favorite_animal = input("What is your favorite animal? ")

if favorite_animal.lower() == "cat":
    print("That's my favorite animal too.")
else:
    print("That one is my favorite")