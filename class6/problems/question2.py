'''
Find the number of distinct elements in alist

example:
arr = [1,2,3,4,1,2,3,100,200,100]
output: 5
'''
arr = [1,2,3,4,1,2,3,100,200,100]
distinct_elements = set(arr)
print(len(distinct_elements))