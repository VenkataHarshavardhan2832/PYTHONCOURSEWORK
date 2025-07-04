# Comprehesions helps in code readablity and reduce length loops in ierable and mutable datastructures(list, dict ,set)

arr = [1,2,3,4,5,6,7,8,9,10]
# writing above array is headache

#comprehension solves it
#[expresssion for i in iterable condition]

arr = [i for i in range(1000)]
print(arr)


# the other way around
arr = []
for i in range(100):
    arr.append(i)

print(arr)

# create an array where all the elements are even till 100

arr = []
for i in range(100):
    if i % 2 == 0:
        arr.append(i)

print(arr)

arr = [i for i in range(100) if i % 2 == 0]
print(arr)

arr = [i * 6 for i in range(1,11)]
print(arr)

# {key expression : value expression for i in iterable condition}
dictionary = {i : i * 6 for i in range(1,11)}
print(dictionary)

# (expression for i in iterable condition)
arr = [1,2,3,4,5,1,2,3,4,5]
set_1 = {num for num in arr}
print(set_1)


