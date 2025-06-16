'''Problem Statement:

Write a Python program that asks the user to enter a number. Then tell them if the number is:

Even or Odd

Positive, Negative, or Zero
sample output:
Enter a number: -3
The number -3 is odd and negative.

'''
number = int(input("Enter a number: "))

if number == 0:
    print("The %d is zero and even" %number )
elif number > 0 and number % 2 == 0:
    print("The %d is even and positive" %number)
elif number > 0 and number % 2 != 0:
    print("The {} is odd and positive".format(number))
elif number < 0 and number % 2 == 0:
    print("The {} is even and negative".format(number))
else:
    print("The {} is odd and negative".format(number))
