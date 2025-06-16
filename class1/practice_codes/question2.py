'''
Write a Python program that asks the user for their name and age, then tells them whether they are a child, teenager, adult, or senior based on the following age groups:

Child: 0–12

Teenager: 13–19

Adult: 20–64

Senior: 65+

sample output:
Enter your name: David
Enter your age: 45
Hi David! At 45 years old, you are an adult.


'''
name = input("What is your name?: ")
age = int(input("What is your age?: "))

if age <= 12:
    print("youa are a Child")
elif age <= 19:
    print("You are a Teenager")
elif age <= 64:
    print("You are a Adult")
else:
    print("You are a Senior")
    