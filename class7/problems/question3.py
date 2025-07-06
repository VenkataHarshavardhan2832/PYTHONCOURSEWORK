'''
Given an array print the multiples of 10's of each element as following

arr = [5,4,3,2,1,2,3,4,5]

{
    5: 50,
    4: 40,
    3 : 30,
    2: 20,
    1: 10,
}

NOTE : The keys shouldn't repeated

'''
arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]
result = {}

for x in arr:
    if x not in result:
        result[x] = x * 10

print(result)