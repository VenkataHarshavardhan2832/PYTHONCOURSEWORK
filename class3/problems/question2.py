'''
Print all the prime numbers between 1 and n, where n is an input number.

Print the sum of the resulting prime numbers
'''
n = int(input("Enter a number: "))

def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
print(is_prime(n))

def print_prime_till(n):
    for i in range(1, n + 1):
        if is_prime(i):
            print(i, end=" ")
print(print_prime_till(100))