"""given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21"""
"""
123 % 10 = 3
123 / 10 = 12
12 % 10 = 2
12 / 10 = 1
1 % 10 = 1
1 / 10 = 0
"""
n = int(input("Enter a number: "))

result = 0

while n > 0:
    digit = n % 10
    result = result * 10 + digit 
    n = n // 10
print(result)