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



def check_even_odd():
    while True :
        try :
            x = int(input("Enter the number :  "))
            if x%2 == 0 :
                return "Number is even"
            else :
                return "Number is odd"
        except ValueError :
            print("invalid input please try again")
result = check_even_odd()
print(result)