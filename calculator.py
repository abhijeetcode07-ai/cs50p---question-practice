# =========================================
# Question:
# Write a Python program to create a simple calculator.
#
# Requirements:
# 1. Take two numbers as input from the user.
# 2. Take an operator input from the user (+, -, *, /).
# 3. Perform the arithmetic operation based on the operator.
# 4. Display the result.
# 5. Handle division by zero with an appropriate message.
#
# Example:
# Enter first number: 10
# Enter operator: /
# Enter second number: 0
# Error: Division by zero is not allowed.
# =========================================


def calculator() :
    while True :
        try :
            num1 = int(input("enter your first number :  "))
            num2 = int(input("enter your second number  :  "))
            operator = input("enter a operator (+,-,*,/)  :  ")
            if operator not in ["+","-","*","/"] :
                    print("please renter the operator")
                    continue
            return num1,num2,operator
        except ValueError :
             print("invalid input , please try again")

def solve(num1,num2,operator) :
     if operator == "+" :
        return num1 + num2
     elif operator == "-" :
         return num1 - num2
     elif operator == "*" :
         return num1*num2
     else :
         return num1/num2

num1,num2,operator = calculator()
print(solve(num1,num2,operator))
      
