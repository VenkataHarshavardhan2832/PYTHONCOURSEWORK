'''
Print the following sequence taking an input n:
n = 2

* * 
* *

n = 5

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

'''
def number(n):

    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
n = int(input("Enter a number: "))
number(n)