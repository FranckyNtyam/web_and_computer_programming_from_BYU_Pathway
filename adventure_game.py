"""
File name: adventure_game.py

Purpose: 05 Prove: Milestone - Adventure Game

"""
# Milestone Requirements
print("------------------------------------------Milestone Requirements--------------------------------------\n")
print("If you don't want your parents to tell you what housework you have to do because you want to choose for yourself, they will give you a list of options from which you can choose one without knowing what type of task it is.\n")
option_housework = input("To find out what kind of housework you'll be doing each day, choose one of those options:\n'HOUSEWORKONE'\n'HOUSEWORKTWO'\n'HOUSEWORKTHREE'\n")
print(" ")

if option_housework.lower() == "houseworkone":
    option_housework_kitchen = input("You pick up houseworkOne, which corresponds to kitchen housework, and you have the option of doing the 'Dishes' or cleaning the 'Floor'.\nchoose option:\n'DISHES'\n'FLOOR'\n")
    if option_housework_kitchen.lower() == "dishes" or option_housework_kitchen.lower() =="floor":
        print("Good job. You have made your choice by yourself. Now respect it.")
    else:
        print("The word you type doesn't correspond to a good word")
elif option_housework.lower() == "houseworktwo":
    option_housework_livingroom = input("You pick up houseworkTwo, which corresponds to living room housework, and you have the option of doing the dusting 'Furniture 'or cleaning the 'Window'.\nchoose option:\n'FURNITURE'\n'WINDOW'\n")
    if option_housework_livingroom.lower() == "furniture" or option_housework_livingroom.lower() == "window":
        print("Good job. You have made your choice by yourself. Now respect it.")
    else:
        print("The word you type doesn't correspond to a good word")
elif option_housework.lower() == "houseworkthree":
    option_housework_toilette = input("You pick up houseworkThree, which corresponds to toilette housework, and you have the option to cleaning the 'Toilette' or leaving your 'Parents' do the choice for you.\nchoose option:\n'TOILETTE'\n'PARENTS'\n")
    if option_housework_toilette.lower() == "toilette" :
        print("Good job. You have made your choice by yourself. Now respect it.")
    elif option_housework_toilette.lower() == "parents":
        print("Good job. your parents will do the good choice for you. They love you.")
    else:
        print("The word you type doesn't correspond to a good word")
else:
    print("Choose the good word en restart the Game\n")
print("---------------------------------------------------------------------------------------------------------------------------------\n")
#Showing Creativity and Exceeding Requirements
print("-------------------------------------------------Showing Creativity and Exceeding Requirements---------------------------------------\n")
option_housework =["houseworkone", "houseworktwo", "houseworkthree"]
prevention_word = "The word you type doesn't correspond of option propose see the next choice."
game_over = "GAME-OVER"
congratulate_word ="Good job. You have made your choice by yourself. Now respect it."
print("You have three different options propose for you.\n If you don't want some of them just Press 'ENTER' on your keyboard")
for housework in range(len(option_housework)):

    if option_housework[housework].lower() == "houseworkone":

        option_housework_kitchen = input("THe first is houseworkOne, which corresponds to kitchen housework, and you have the option of doing the 'Dishes' or cleaning the 'Floor'.\nchoose option:\n'DISHES'\n'FLOOR'\n")

        if option_housework_kitchen.lower() == "dishes" or option_housework_kitchen.lower() =="floor":
            print(f"{congratulate_word}\n{game_over}")
            break
        else:
            print(prevention_word)
            continue
    elif option_housework[housework].lower() == "houseworktwo":
       option_housework_livingroom = input("THe second is houseworkTwo, which corresponds to living room housework, and you have the option of doing the dusting 'Furniture 'or cleaning the 'Window'.\nchoose option:\n'FURNITURE'\n'WINDOW'\n")
       if option_housework_livingroom.lower() == "furniture" or option_housework_livingroom.lower() == "window":
          print(f"{congratulate_word}\n{game_over}")
          break
       else:
          print(prevention_word)
          continue
    elif option_housework[housework].lower() == "houseworkthree":
       option_housework_toilette = input("The last is houseworkThree, which corresponds to toilette housework, and you have the option to cleaning the 'Toilette' or leaving your 'Parents' do the choice for you.\nchoose option:\n'TOILETTE'\n'PARENTS'\n")
       if option_housework_toilette.lower() == "toilette" :
         print(f"{congratulate_word}\n{game_over}")
       elif option_housework_toilette.lower() == "parents":
         print("Good job. your parents will do the good choice for you. They love you.\nGame-Over")
         break
       else:
         print(prevention_word)
         continue
    else:
     print("Choose the good word en restart the Game\n")