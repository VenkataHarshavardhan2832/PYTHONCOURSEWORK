# while loop works the same bbut it executes until some condition is false

# while condition which return boolean value::

i = 1
while i <= 100:
    print(i, end=" ")
    i += 1

print("\n")
for i in range(1,100):
    print(i, end=" ")
    if i == 10:
        break

print("\n")

for i in range(1,100):
    print(i, end=" ")
    if i == 10:
        continue # continue is negation of break


# given a number you need to print if the number is prime or not

#2 -> 2
#13 -> 13
#12 -> 2, 3, 4, 6, 12

# 14 -> 2,7 

# we are iteratinf from 2 till n -1  anc checking whether i  value is n % i is giving zero or not

n = int(input("Enter a number to check if it is prime or note: "))

prime = True
for i in range(2,n):
    if n % i == 0:
        prime = False
        print("{} is not a prime number".format(n))
        break

if prime == True:
    # if prime is still true then it means that the number is prime
    print("{} is a prime number".format(n)) 

print("\n")


# You are given a number n, you need to print of the number is armstrong or not

# 153 -> 1 ** 3 + 5 **3 + 3**3 = 153 armstrong
# 140 -> 1 ** 3 + 4 ** 3 + 0 ** 3 = 65 not armstrong

n = int(input("Enter a number to check if it is armstrong or not: "))

# 153 % 10 = 3
# 153 / 10 = 15
# 15 % 10 = 5
# 15 / 10 = 1
# 1 % 10 = 1
# 1 / 10 = 0
sum = 0
m = n # storing the original number to compare later
while n > 0:
    digit = n % 10 # getting the digit
    sum += digit ** 3 # adding the cube of the digit to the sum
    n = n // 10 # removing the last digit from the number

if sum == m:
    print("The number is armstrong")
else:
    print("The number is not armstrong")







