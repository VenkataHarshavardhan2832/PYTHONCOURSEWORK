# Dictionaries is a datatype which you use to store key value pairs

#Examplee
'''
dictionary = {
    'harsha' : 18,
    'amrath' : 22
}
'''

arr = [1,2,3,4,5,6]
arr.append(5) # o(1)
arr.insert(4,6) # o(n) where n is the length
arr.remove(2) # o(n)


dictionary = {
    1 : 'python',
    2: 'c++',
    'harsha': 'java',
    'Harsha' : 'python'
}
# most of the cases you keep it  homogenous
print(type(dictionary))

print(dictionary['harsha'])
print(dictionary["Harsha"])
# keys are case sensitive 

# Keys are immutatble but values are mutable
print(dictionary[1])
dictionary[1] = "learning"
print(dictionary[1])

# Insertion , deletion , updating values happens in constant time o(1)
# Delete operation directly deletes the value it doesnt return anything
del dictionary[1]
print(dictionary)
# pop also deletes but stores or return the deleted value
val = dictionary.pop(2)
print(val)
print(dictionary)

# clear deletes all the vlaues fomr the dictionary

dictionary.clear()
print(dictionary)


dictionary = {
    1: 10,
    2: 20,
    3: 30,
    4: 40
}


# Iterate through keys

for key in dictionary:
    print(key,end=" ")
print("\n")

# Iterate through all the values in the dictionary

for values in dictionary.values():
    print(values,end=" ")
print("\n")

# Iterate through keys and values at the same time

for key,value in dictionary.items():
    print(f"{key}:{value}",end=" ")
print("/n")

dictionary[4]
for key in dictionary:
    print(f"{key}:{dictionary[key]}",end=" ")
print("\n")

# Nested dictionary

dictionary = {
    1 :10,
    2:20,
    3: {
        1: 'harsha',
        2: "ram"
    },
    4: [1,2,3,4,5]
}
print(dictionary[3][1])

for key in dictionary:
    if isinstance(dictionary[key],dict):
        for inside_keys in dictionary[key]:
            print(f"{inside_keys}:{dictionary[key][inside_keys]}",end=" ")
    if isinstance(dictionary[key],list):
        print("printing the list values",dictionary[key])
    print("\n")
print("\n")

# given an array contains values count the number of repitions of each value

# example : arr[1,2,3,100,200,300,300,200,400,1,2] {1: 2,2:2,100:1,200:2,300:2,400:1}

arr = [1,2,3,100,200,300,300,200,400,1,2]
dictionary_count = {}
for  i in arr:
    if i in dictionary_count.keys():
        dictionary_count[i] = dictionary_count[i] + 1
    else:
        dictionary_count[i] = 1
    
print(dictionary_count)