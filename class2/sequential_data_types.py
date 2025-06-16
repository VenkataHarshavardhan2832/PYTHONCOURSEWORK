# https://www.geeksforgeeks.org/python/python-string/

# Sequential data types in python are used to store collections of items in an order

# sequential data types - list, tuple,string

# strings - used to store sequence of characters(text)

# How you access a character in a string

# HARSHA
# 012345  - indexing start from zero
# -6-5-4-3-2-1
name = "Harsha"

print("ACcessing first a",name[1],name[-5])
print("ACcessing second h",name[4],name[-2])

surname = "Venkata"
#concatenation - joining two strings together
full_name = name + " " + surname

print("Full name :",full_name)

# string are immutable - cannot be changed

# name[0] = "a" # TypeError: 'str' object does not support item assignment

# formatting the string
output = "Your full name is : {}".format(full_name)
print(
    output
)

# lower() amd upper()

name = name.upper()
print("Uppercase name:", name)
name = name.lower()
print("Lowercase name:", name)

# length of a string

print(len(name)) # length of the string

# slicing a string

# string[start:end:step]

print("slicing a string and getting first three charecters:",name[0:3]) # harsha - 0 is inclusive and 3 is exclusive(wont pick the last index)

print("slcicing a string with negative index:", name[-6:-3]) # harsha - -6 is inclusive and -3 is exclusive

print("Slicing while skipping characters:", name[0:6:3]) # harsha - 0 is inclusive, 6 is exclusive and 2 is the step size

print("Reversing a string:", name[::-1]) # reversing the string - step size is -1

name1 = "Harsha"
name2 = "Harsha"

# comparing strings
if name1 == name2:
    print("Both names are same")
else:
    print("Both names are different")


# checking if a certain string present in another string - in  and not in operators

str1 = "Harsha"
str2 = "am"

if str2 in str1:
    print(f"{str2} is present in {str1}")
else:
    print(f"{str2} is not present in {str1}")

if str2 not in str1:
    print(f"{str2} is not present in {str1}")
else:
    print(f"{str2} is present in {str1}")

str1 = str1 + " " + str2  # concatenating two strings

