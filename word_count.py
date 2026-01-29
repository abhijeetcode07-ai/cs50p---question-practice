# =========================================
# Question:
# Write a Python program to count the number of words in a sentence.
#
# Requirements:
# 1. Take a sentence as input from the user.
# 2. Split the sentence into words.
# 3. Count the total number of words.
# 4. Print the word count.
#
# Example:
# Input: "I love programming"
# Output: 3
# =========================================


def count_word() :
    sent = input("Enter you sentence :  ")
    word = sent.split()
    return len(word)

result = count_word()
print("Total number of words in the sentence is :  ",result)