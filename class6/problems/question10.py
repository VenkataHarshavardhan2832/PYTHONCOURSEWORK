'''
Explore and write code for this algorithms

1. Bubble sort
2. Selection sort
3. Insertion sort

write code and understand it!
'''
arr = [3,2,4,5,1]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        key = arr[i]
        if arr[i] < arr[j]:
            arr[i] = arr[j]
            arr[j] = key

print(arr)

print(" ")

arr = [3,2,5,4,1]
def insertion_sort(arr):
    for i in range(0,len(arr)):
        key = arr[i]
        # key = 4
        j = i-1
        while j >= 0 and arr[j] < key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)

insertion_sort(arr)

print(" ")

arr = [3,2,4,5,1]
def selection_sort(arr):
    for i in range(0, len(arr)):
        min_index = i
        min_number = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[min_index]:
                min_index = j
        key = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = key
       
    print(arr)
          
selection_sort(arr)   