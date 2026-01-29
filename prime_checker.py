# =========================================
# Question:
# Write a Python program to check if a number is prime or not.
#
# Requirements:
# 1. Take an integer input from the user.
# 2. Check whether the number is prime.
# 3. Print "Prime" if it is prime, otherwise print "Not Prime".
#
# Example:
# Input: 13
# Output: Prime
# =========================================


def is_prime(n) :
    
    if n<2 :
        return False
    for i in range(2,n) :
        if n%i == 0 :
            return False
    return True

while True :
    try :
        num = int(input("enter the number to check :  "))
        break
    except ValueError :
        print("please try again")

result = is_prime(num)
print(result)