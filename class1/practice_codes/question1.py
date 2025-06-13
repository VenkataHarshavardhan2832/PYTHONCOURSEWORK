"""Write a Python program that takes a student's name and score (out of 100) as input. The program should then print a personalized message with the student's grade based on the following rules:

A: 90–100

B: 80–89

C: 70–79

D: 60–69

F: Below 60
CLEAVEREASE PYTHON HANDSON"""

name = input("Student Name: " )
score = int(input("Student Score: "))

if score >= 90:
    print("Hi %s your score is %d. so your grade is A" % (name, score))
elif score >= 80:
    print("Hi %s your score is %d. so your grade is B" % (name, score))
elif score >= 70:
    print("Hi %s your score is %d. so your grade is C" % (name, score))
else:
    print("Hi %s your Failed in your exam" % name)

