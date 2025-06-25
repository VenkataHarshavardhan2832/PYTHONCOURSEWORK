'''
use while loop to print even numbers from 1 to n
'''
n = int(input("Enter a number: "))

def is_even(n):
    if n % 2 == 0:
        return True
    return False
i = 1
while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1


