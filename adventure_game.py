"""
File name: adventure_game.py

Purpose: 05 Prove: Milestone - Adventure Game

"""
# Milestone Requirements
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("If you don't want your parents to tell you what housework you have to do because you want to choose for yourself, they will give you a list of options from which you can choose one without knowing what type of task it is.\n")
option_housework = input("To find out what kind of housework you'll be doing each day, choose one of those options:\n'houseworkOne'\n'houseworkTwo'\n'houseworkThree'\n")
print(" ")

if option_housework.lower() == "houseworkone":
    option_housework_kitchen = input("You pick up houseworkOne, which corresponds to kitchen housework, and you have the option of doing the 'Dishes' or cleaning the 'Floor'.\nchoose option:\n'Dishes'\n'Floor'\n")
    if option_housework_kitchen.lower() == "dishes" or "floor":
        print("Good job. You have made your choice by yourself. Now respect it.")
    else:
        print("The word you type doesn't correspond to a good word")
# end Milestone Requirements Lesson 5
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
elif option_housework.lower() == "houseworktwo":
    option_housework_livingroom = input("You pick up houseworkTwo, which corresponds to living room housework, and you have the option of doing the dusting 'Furniture 'or cleaning the 'Window'.\nchoose option:\n'Furniture'\n'window'\n")
    if option_housework_livingroom.lower() == "furniture" or "window":
        print("Good job. You have made your choice by yourself. Now respect it.")
    else:
        print("The word you type doesn't correspond to a good word")
elif option_housework.lower() == "houseworkThree".lower():
    option_housework_toilette = input("You pick up houseworkThree, which corresponds to toilette housework, and you have the option to cleaning the 'Toilette' or leaving your 'Parents' do the choice for you.\nchoose option:\n'Toilette'\n'Parents'\n")
    if option_housework_toilette.lower() == "toilette" :
        print("Good job. You have made your choice by yourself. Now respect it.")
    elif option_housework_toilette.lower() == "parents":
        print("Good job. your parents will do the good choice for you. They love you.")
    else:
        print("The word you type doesn't correspond to a good word")
else:
    print("Choose the good word en restart the Game")