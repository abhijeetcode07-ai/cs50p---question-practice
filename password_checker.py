# =========================================
# Question:
# Write a Python program to create a simple password checker system.
#
# Requirements:
# 1. Store a predefined password inside the program.
# 2. Ask the user to enter the password.
# 3. If the password is correct:
#       print "Access Granted".
# 4. If the password is incorrect:
#       print "Access Denied".
# 5. Allow the user multiple attempts until the correct password is entered.
# 6. Use loops and conditional statements to implement the logic.
#
# Example:
# Enter password: 1234
# Access Denied
# Enter password: admin@123
# Access Granted
# =========================================


def check_password() :
        password = input("enter the password :  ")
        
        if len(password)<8 :
            return False
        
        has_alpha = False
        has_digit = False

        for ch in password :
            if ch.isaplha() :
                has_alpha = True
            if ch.isdigit() :
                has_digit = True

        

        if has_alpha  and has_digit :
            return "strong"
        else :
             return "weak"

result = check_password()
print(result)