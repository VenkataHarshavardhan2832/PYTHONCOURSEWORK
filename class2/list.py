# https://www.geeksforgeeks.org/python/python-lists/

# Note : Before studying list study about strings
# list is a sequential data types which is mutable and contains heterogeneous data types and is ordered.

# lists are dynamic
#string are dynamic

# List also follows same indexing and slicing as strings

hetero_list = [1, 2.5, "Harsha", True, None]

print("accessing the 3rd element in the list:", hetero_list[2])  # accessing the 3rd element in the list

sub_list = hetero_list[0:3] # accessing first 3 elements in the list
print("accessing first 3 elements in the list : ", sub_list)  

reverse_list = hetero_list[::-1]  # reversing the list

print("Reversing the list:", reverse_list)

# append ,extent,insert,remove,pop,sort,reverse

hetero_list.append("New Element")  # appending a new element to the list

hetero_list.extend([3, 4, 5])  # extending the list with new elements(adding multiple values)

print(hetero_list)

hetero_list.insert(2,"Harsha") # insert(index, value) - inserting a new element at the particular index of the list

print(hetero_list)

hetero_list.remove("Harsha") # Removes the first occurrence of the value from the list
# hetero_list.remove(10) Throws an error

print(hetero_list)

hetero_list.pop()    # removes the last element from the list and returns it

print("After pop operation:", hetero_list)

scores = [100,10,30,60,90]

sorted_scores = scores.sort()  # sorts the list in ascending order
print("Sorted scores:", scores)  # sort() modifies the original list in place

reverse_list = scores.reverse()  # reverses the list in place
print("Reversed scores:", scores)  # reverse() modifies the original list in place

