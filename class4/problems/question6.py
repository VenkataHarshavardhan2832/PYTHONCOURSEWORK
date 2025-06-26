"""
You are given an integer n. You need to find all the divisors of n. Return all the divisors of n as an array or list in a sorted order.


A number which completely divides another number is called it's divisor.
Example:
Input: n = 6

Output = [1, 2, 3, 6]

Explanation: The divisors of 6 are 1, 2, 3, 6.
"""
n = int(input("Enter a number: "))
divisors = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.extend([i])
        
        print(n, divisors)
