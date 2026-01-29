# =========================================
# Question:
# Write a Python program to check if a number is even or odd.
#
# Requirements:
# 1. Take an integer input from the user.
# 2. Check if the number is even or odd.
# 3. Print "Even" if the number is even, otherwise print "Odd".
#
# Example:
# Input: 7
# Output: Odd
# =========================================



def get_int(prompt) :
    while True :
        try :
            num = int(input(prompt))
            return num
        except ValueError :
            print("invalid input, please try again")
result = get_int("Enter your number :  ")
print(result)