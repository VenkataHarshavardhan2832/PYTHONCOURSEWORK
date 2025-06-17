'''
Write a program that takes a string as input and checks whethere it is a palindrome or not.

example:
MARKRAM
MARKRAM

RACECAR
RACECAR

HARSHA
AHSRAH -this is not a palindrome

output:
MARKRAM is a palindrome

HARSHA is not a palindrome
'''
text = input("What is your name: ")

reversed_text = text[::-1]
if text == reversed_text:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
