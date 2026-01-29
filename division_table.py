# =========================================
# Question:
# Write a Python program to generate the division table of a number.
#
# Requirements:
# 1. Take an integer input from the user.
# 2. Print the division results from 1 to 10.
# 3. Each line should display:
#       number / i = result
# 4. Use a loop to generate the table.
#
# Example:
# Input: 6
# Output:
# 6 / 1 = 6.0
# 6 / 2 = 3.0
# 6 / 3 = 2.0
# ...
# 6 / 10 = 0.6
# =========================================



def main() :
    while True :
        try :
            num = int(input("Enter the number :  "))
            if num == 0 :
                print("zero division is not allowed")
                continue
            return divide_table(num)
        except ValueError :
            print("invalid input please try again ")
        
def divide_table(n) :
    for i in range(1,11) :
        print(f"{n}/{i} = {n/i}")
         
main()