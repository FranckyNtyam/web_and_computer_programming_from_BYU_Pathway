"""
File: word_games.py
Author: Brother Francky Ntyam

Purpose: 02 Prove: Assignment - Word Games.

This program also contains a way to Showing Creativity and Exceeding Requirements.
"""

print("Please enter the following:")
print()

#Ask user a series of words 
adjective = input("Enter some adjective: ")
animal = input("Enter some animal: ")
first_verb = input("Enter some first verb: ")
exclamation = input("Enter some exclamation: ")
second_verb = input("Enter some second verb: ")
third_verb = input("Enter some third verb: ")
print()
print("Your story is:\n")
print(f"The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {first_verb}  down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all I could think to do was to {second_verb} over and over. Miraculously, that caused it to stop, but not before it tried to {third_verb} right in front of my family.")

#Showing Creativity and Exceeding Requirements
print("---------------------------------------")
#Ask user a series of words 
adjective = input("Enter some adjective: ")
animal = input("Enter some animal: ")
first_verb = input("Enter some first verb: ")
exclamation = input("Enter some exclamation: ")
second_verb = input("Enter some second verb: ")
third_verb = input("Enter some third verb: ")
#ask more information
my_list=['a','e','i','o','u']
noun = input("Enter some noun: ")
article = " "
if noun[0] == my_list[0] or noun[0] == my_list[1] or noun[0] == my_list[2] or noun[0] == my_list[3] or noun[0] == my_list[4]: 
    article = input("Enter article \"an\": ")
else:
    article = input("Enter article \"a\": ")

sentence= f"I am {article} {noun}."
print(sentence)
print()
print("Your story is:\n")
#display the story using the keyword arguments(end) of print() function and add variable sentence in the story.
print("The other day, I was really in trouble.", end=" " )
print(f"It all started when I saw a very {adjective} {animal} {first_verb}  down the hallway.", end=" ")
print(f"\"{exclamation.capitalize()}!\" I yelled. But all I could think to do was to {second_verb} over and over.", end=" ")
print(f"Miraculously, that caused it to stop, but not before it tried to {third_verb} right in front of my family. {sentence}")

print("---------------------------------------")