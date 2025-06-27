'''
Given an array and an element find the element exists in an array,
array is sorted in ascending order

arr = [1,2,3,4,5] element = 5

low = 0
high = len(arr)-1 = 4
mid = (high + low )/ 2 = 2

now i ll compare 

if arr[mid] < element:
    low = mid + 1 // 3

if arr[mid] > element: 
    high = mid - 1


output: true
'''

'''
n = 2
* *
* *
'''

def print_pattern(n):
    # o(n * n)
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print("\n")
print_pattern(5)
arr = [1,2,3,4,5]


ele = 5
def check_ele(arr,element):
    # o(n) - asymtotic notation
    for i in arr:
        if i == element:
            return True
    return False

print(check_ele(arr,element=ele))



'''
Given an arrrya the numbers in the array are from 0-9, count how many times each number got repeated
'''
arr = [0,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,9,8,0] # len(arr) - k, n is numbers range

def way1(arr):
    for i in range(10):# o(n)
        count = 0 # o(1) space
        for j in arr: # o(k*n)
            if i == j:
                count += 1
        print(i , count, end = " ")
        print("\n")

way1(arr)




def way2(arr):
    count = [0,0,0,0,0,0,0,0,0,0] # o(n) is the extra space here
    for j in arr: # j is alway betwreen 0-9. o(k) is the complexity where k is length of array
        count[j] += 1
    
    print("#####")
    for i in range(len(count)):
        print(i , count[i], end=" ")
        print("\n")


way2(arr)


def binary_search(arr,ele):
    # o(log(n)) < o(n)
    low = 0
    high = len(arr)-1
    mid = int((low + high) / 2)

    while low >= 0 and high < len(arr):
        if arr[mid] < ele:
            low = mid + 1
        
        elif arr[mid] > ele:
            high = mid - 1

        elif arr[mid] == ele:
            return True
        
        mid = int((low + high) / 2)
        print(mid)
    
    return False

print(binary_search([1,2,3,4,5],10))


