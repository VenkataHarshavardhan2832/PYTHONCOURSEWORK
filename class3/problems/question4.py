'''given an integer n print the following pattern

n = 2
output:
*
* *


n = 3 
output:
*
* *
* * *

n = 5
output:
*
* *
* * *
* * * *
* * * * *
'''
def number(n):
    for i in range(1, n+1):
        for j in range(i):
            print("*", end=" ")
        print()
n = int(input("Enter a number: "))
number(n)