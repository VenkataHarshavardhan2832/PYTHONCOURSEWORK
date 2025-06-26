"""Take a input from the user which is int
print the number of digits in the number 
count the number of even digits

example:
input: 123
output: 3
123 % 10 = 3
123 / 10 = 12
12 % 10 = 2
12 / 10 = 1
1 % 10 = 1
1 / 10 = 0

example
input: 12345
output : 5

"""
n = int(input("Enter a number: "))

def even_count(n):
    count = 0
    while n > 0:
        digit =  n % 10
        if digit % 2 == 0:
            count += 1
        n = n // 10
    return count
digit_count = len(str(n))
print("Number of digits:", digit_count)
print(even_count(n))
