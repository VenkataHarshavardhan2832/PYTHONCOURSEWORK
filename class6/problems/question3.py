'''
Remove distinct elements from a list

arr = [1,2,3,4,1,2,3]
output: [1,2,3,4]
'''
"""arr = [1, 2, 3, 4, 1, 2, 3]

arr.remove(1)
arr.remove(2)
arr.remove(3)


print(arr)"""

arr = [1, 2, 3, 4, 1, 2, 3]
new_arr = []

for i in arr:
    if i not in new_arr:
        new_arr.append(i)

print(new_arr)
