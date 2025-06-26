"""Given a number as input print YES if number is palindrome and NO if not

09:42
exmaple:c
Input: 12321
output: YES

input: 123
output: NO
"""
number = input("Enter a number: ")  

reversed_number = number[::-1]
if number == reversed_number:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
