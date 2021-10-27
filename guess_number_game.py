"""
file name: guess_number_game.py
Purpose: Guess My Number Game.
"""

import random
def guess_my_magic_number():
   
   magic_number = random.randint(1, 100)
   guess_number = int(input("What is your guess? "))
   number_of_guess = 1
   while guess_number != magic_number:
      if guess_number < magic_number :
         print("Higher")
      elif guess_number > magic_number :
         print("Lower")
      guess_number = int(input("What is your guess? "))
      number_of_guess += 1
   print("You guessed it!")
   print(f"the number of guess is : {number_of_guess}")
   print("Game Over")
guess_my_magic_number()
answer_of_user = input("Do you want to play again? ")
while answer_of_user.lower() == "yes" :
   guess_my_magic_number()
   answer_of_user = input("Do you want to play again? ")
print("Thank you to be passed")
