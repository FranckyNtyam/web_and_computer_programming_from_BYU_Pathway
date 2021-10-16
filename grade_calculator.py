"""
file name: grade_calculator.py

Purpose: create Grade Calculator
"""
# Core requirements
grade_percentage = float(input("Enter your grade percentage: "))

# if grade_percentage >= 90 :
#     print("A")
# elif grade_percentage >= 80 :
#     print("B")
# elif grade_percentage >= 70 :
#     print("C")
# elif grade_percentage >= 60 :
#     print("D")
# else :
#     print("F")

if grade_percentage >= 90 and grade_percentage % 10 >= 7:
    letter = "A+"
elif grade_percentage >= 90 and grade_percentage % 10 <= 3:
    letter = "A-"
elif grade_percentage >= 90 and grade_percentage % 10 > 3 and grade_percentage % 10 < 7:
    letter = "A"      
elif grade_percentage >= 80 and grade_percentage % 10 >= 7:
    letter = "B+"
elif grade_percentage >= 80 and grade_percentage % 10 <= 3:
    letter = "B-"
elif grade_percentage >= 80 and grade_percentage % 10 > 3 and grade_percentage % 10 < 7:
    letter = "B"   
elif grade_percentage >= 70 and grade_percentage % 10 >= 7:
    letter = "C+"
elif grade_percentage >= 70 and grade_percentage % 10 <= 3:
    letter = "C-"
elif grade_percentage >= 70 and grade_percentage % 10 > 3 and grade_percentage % 10 < 7:
    letter = "C"   
elif grade_percentage >= 60 and grade_percentage % 10 >= 7:
    letter = "D+"
elif grade_percentage >= 60 and grade_percentage % 10 <= 3:
    letter = "D-"
elif grade_percentage >= 60 and grade_percentage % 10 > 3 and grade_percentage % 10 < 7:
    letter = "D"   
elif grade_percentage < 60 and grade_percentage % 10 >= 7:
    letter = "F+"
elif grade_percentage < 60 and grade_percentage % 10 <= 3:
    letter = "D-"
else :
    letter = "F"
print(letter) 

if grade_percentage >= 70 :
    print("Congratulation you pass")
else :
    print("sorry you don't pass but you can do some effort you will and never give up")
