# =========================================
# Question:
# Write a Python program to find the maximum of three numbers.
#
# Requirements:
# 1. Take three numbers as input from the user.
# 2. Compare the numbers to find the largest.
# 3. Print the largest number.
#
# Example:
# Input: 10, 25, 7
# Output: The largest number is 25
# =========================================



def find_max() :
    while True :
        try :
            x = int(input("enter the first number :  "))
            y = int(input("enter the second number :  "))
            z = int(input("enter the third number :  "))
            if x == y == z :
                return "All are equal"
            elif (x>=y and x>z) or (x>=z and x>y) :
                return x
            elif (y>=x and y>z) or (y>=z and y>x) :
                return y
            else :
                return z
        except ValueError :
            print("invalid input , please try again ")


    
result = find_max()
print("Maximum number is :  ",result)