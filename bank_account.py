"""
File name: bank_acccount.py
Author: Ntyam Adjomo FRancky Ludovic

Purpose: Sometimes you have two lists that you want to keep in sync with each other. For example, in this assignment, you will track bank accounts and the balances in each one.
"""
bank_account_name_list = []
bank_account_balance_list =[]
print("Enter the names and balances of bank accounts (type: quit when done)")

bank_account_name =""
bank_account_balance =0

while bank_account_name.lower() != "quit":
    bank_account_name = input("What is the name of this account? ")
    if bank_account_name != "quit" :
        bank_account_balance = float(input("What is the balance? "))
        bank_account_name_list.append(bank_account_name)
        bank_account_balance_list.append(bank_account_balance)

print("\nAccount Information:")
total = 0
average = 0
for index in range(len(bank_account_name_list)):
    print(f"{index}. {bank_account_name_list[index]} - ${bank_account_balance_list[index]}")
    total += bank_account_balance_list[index]

print(f"\nTotal: {total}")
print(f"Average: {round((total / len(bank_account_balance_list)), 2)}")
