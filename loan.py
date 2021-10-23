"""
file name: loan.py

Purpose: Checkpoint: Qualifying for a loan.
"""
"""
the program will ask user different information 
to know if he or she eligible for the loan
"""
print("For a rating from 1–10 on the following:\n")

loan = float(input("How large is the loan? "))
credit_history = float(input("How good is your credit history? "))
income = float(input("How high is your income? "))
down_payment = float(input("How large is your down payment? "))
print("")
if loan == 5 and credit_history == 7 and income == 7 :
    can_get_loan = True
    if loan == 5 and (credit_history == 7 or income == 7) and down_payment == 5 :
        can_get_loan = True
    
elif loan >  5 and credit_history < 4 :
    can_get_loan = False
    if loan > 5 and credit_history < 4 and (income == 7 or down_payment == 7) or income == 4 and down_payment == 4  :
        can_get_loan = True
else:
    can_get_loan = False


print(can_get_loan)
