# =========================================
# Question:
# Write a Python program to simulate an ATM machine.
#
# Requirements:
# 1. Initialize a balance amount (e.g., 1000).
# 2. Show a menu with the following options:
#    1. Check Balance
#    2. Deposit Money
#    3. Withdraw Money
#    4. Exit
# 3. Based on user choice, perform the action:
#    - For deposit, ask the amount and add to balance.
#    - For withdrawal, ask the amount and subtract if sufficient balance is available.
#    - For exit, end the program.
# 4. Display appropriate messages for each operation.
#
# Example:
# Menu:
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Exit
# Enter choice: 2
# Enter deposit amount: 500
# Deposit successful. New balance is 1500
# =========================================


def atm():

    balance = 1000   # state outside loop

    while True:

        print("\n1 Balance")
        print("2 Deposit")
        print("3 Withdraw")
        print("4 Exit")

        command = input("Enter choice: ")

        if command == "1":
            print("Balance:", balance)

        elif command == "2":
            amount = int(input("Deposit amount: "))
            balance += amount

        elif command == "3":
            amount = int(input("Withdraw amount: "))
            if amount > balance:
                print("Insufficient funds")
            else:
                balance -= amount

        elif command == "4":
            print("Exited")
            break

        else:
            print("Invalid choice")


atm()