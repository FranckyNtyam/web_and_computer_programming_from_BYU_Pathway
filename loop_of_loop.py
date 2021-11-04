"""
File name: loop_of_loop.py

Purpose: write a program that uses loops within loops to generate multiplication tables.

"""
row_and_columns = int(input("How many columns and rows do you want in your multiplication table? "))
for i in range(1, row_and_columns + 1):
    for j in range(1, row_and_columns + 1):
        print(f"{i*j:3}", end=" ")
    print("")     
   