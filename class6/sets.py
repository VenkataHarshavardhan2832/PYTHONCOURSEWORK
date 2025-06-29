
# find distinct elements in an arrays : arr = [1,2,3,4,5,1,2,3,6,7]

arr = [1,2,3,100,200,300,300,200,400,1,2]
dictionary_count = {}
for  i in arr:
    if i in dictionary_count.keys():
        dictionary_count[i] = dictionary_count[i] + 1
    else:
        dictionary_count[i] = 1
    
for key in dictionary_count:
    print(key, end=" ")

print("\n")


# sets store distinct values - sets are unordered Note Order is not preserved in a set

set_1 = {1,2,3,100,200,300,300,200,400,1,2}
print(set_1)
# print(set_1[0]) throws an error 'set' object is not subscriptable

set_2 = set("harsha")
set_3 = {"harsha"}
print(set_2)
print(set_3)
tup = ("harsha","is","harsha")
print(set(tup))

# you can add elements to a set

set_4 = {1,2,3,4,5}
set_4.add(6)
set_4.add(1)
print(set_4)

# adding multiple values at the same time

set_4.update([1,2,3,4,5,6,7,8,9])
print(set_4)

# only way to access values is to iterate

for value in set_4:
    print(value,end=" ")

print("/n")

# removing values from the set

set_4.remove(9) # remove throws a error if value is not present

set_4.discard(10) # this wiill remove element but dont throw a error if the value is not in the list

set_4.clear()
print(set_4)

# Advantages of sets - distinct elements , faster lookup if some element exist in a ds o(1),mutablity,mathematics of sets

# if i want to check some number exist in a list or not

list_1 = [1,2,3,4,5,6,7]
print(7 in list_1) # o(n)

set_1 = set(list_1)
print(7 in set_1) # o(1)

