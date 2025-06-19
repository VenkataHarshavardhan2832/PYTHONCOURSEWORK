# Sequential data types - tuple is also a sequential data type like list(heterogenous data types,mutable,ordered) but typle is immutable

tup = (1,2.5,"Harsha",True,None)

# indexing and slicing works same here tup[start:end:step]

print("Printing the first element:",tup[0])

# tup[0] = 10  # TypeError: 'tuple' object does not support item assignment explains that tuples are immutable

# remove , pop,append,insert,extend,sort,reverse 

# tup.remove() # remove doesnt work for tuple
# tup.pop()  # pop works for tuple but it will throw an error as tuples are immutable
# tup.append("New Element")
# tup.insert(2,"Harsha")  # insert(index, value) - inserting a new element at the particular index of the tuple but doesnt support

tup = (5,4,3,2,1)
# sorted_tuple = tup.sort() # sort is not supported

tup = tup[:3] # slicing is supported
tup = tup[::-1]
print(tup)

print(sum(tup)) # sum of all elements
print(max(tup)) # maximum element in the tuple
print(min(tup)) # minimum element in the tuple
print(len(tup)) # length of the tuple
