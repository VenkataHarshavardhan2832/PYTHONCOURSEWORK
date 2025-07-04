'''
Given an array find the maximum element in the list without using max inbuilt-function in python

functions -> user defined functions(You write this functions) , inbuilt functions max(),sum(), items(),keys() 

example : [1,2,3,4,5,10,-1,-2]
ans = 10

Write an another function minmum_element which finds the minimum element in the array
example : [1,2,3,4,5,10,-1,-2]
ans = -2

'''

arr = [1,2,3,4,5,10,-1,-2]

def max_in_an_array(arr):
    max_element = 0
    for num in arr:
        if num > max_element:
            max_element = num # 10
    return max_element

print(max_in_an_array(arr))