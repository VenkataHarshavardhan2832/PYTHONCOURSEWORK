'''
Explore and write code for this algorithms

1. Bubble sort
2. Selection sort
3. Insertion sort

write code and understand it!
'''

# Bubbble sort 

'''
4,3,5,2,1
i = 0
3,4,5,2,1
j = 2
j = 3
2,4,5,3,1
j=4
1,4,5,3,2
i= 1
j=2
j=3
1,3,5,4,2
j=4
1,2,5,4,3
i=3
1,2,3,5,4

i =4
1,2,3,4,5
'''


for j in range(5,0,-1):
    print(j)

arr = [4,3,5,2,1]
arr =[10,9,8,7,6,5,4,3,2,1]

arr = [1,2,3,4,5]
# o (n*n) = o(n^2)
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        key = arr[i]
        if arr[i] > arr[j]:
            arr[i] = arr[j]
            arr[j] = key

print(arr)


'''
arrr = [4,2,3,1,5]
key = 4 [0]no elementbefore it that is greater than 4 ill leave
key = 2 [1]
[2,4,3,1,5]
key = 3[2]
[2,3,4,1,5]
key = 1[3]
[1,2,3,4,5]
key = 5[4]
[1,2,3,4,5]

Lets see for sorted array
[1,2,3,4,5]
'''
def insertion_sort(arr):
    for i in range(0,len(arr)):
        key = arr[i]
        # key = 4
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)

insertion_sort([5,4,3,2,1])
insertion_sort([5,4,2,1,6,3])

'''
arr = [4,2,5,1,3]
i = 0
[1,2,5,4,3]
i = 1
1,2,5,4,3
i = 2
1,2,3,4,5

'''
"""def selection_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):"""
print("###")
def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        min_number = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        key = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = key
        print(arr)
    print(arr)
          
selection_sort([4,2,5,1,3])   