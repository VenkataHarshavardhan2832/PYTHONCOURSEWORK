# print all the numbers from 1 to 100

# using for loop
# range returns sequence of integers from start to end - 1 by step
for i in range(1,101):
    print(i, end=" ")

print("\n")

# print the sum of all numbers from 1 to 100
sum = 0
for i in range(1,101):
    # sum = 0 + 1
    # sum = 1 + 2
    # sum = 3 + 3
    print(sum,end=" ")
    sum = sum + i

print(sum)

sum = (100 * (100  + 1)) / 2

print(sum)

# I want to print all the subarrays in the given list
# subarray are contiguous elements in the list
list = [1,2,3,4]
# all the subarrays [1] [1,2] [1,2,3] [1,2,3,4] [2] [2,3] [2,3,4] [3] [3,4] [4]
length = len(list) # 4

for i in range(0,length):
    for j in range(i,4):
        print(list[i:j+1],end="")
    print("\n")

# using for loop with list, tuple string
string = "harsha"
for i in range(len(string)):
    print(string[i],end=" ")
print("\n")

for i in string:
    print(i, end=" ")

print("\n")

for i in list:
    print(i, end=" ")
print("\n")

tup = (1,2.5,"Harsha",True,None)
for element in tup:
    print(element, end=" ")




