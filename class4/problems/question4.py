"""Take a input form the user and count the number of odd digits in that number
example:
input: 123
output: 2

"""
n = input("Enter a number: ")
count = 0

for digit in n:
    if int(digit) % 2 != 0:

        count += 1

print(count)
