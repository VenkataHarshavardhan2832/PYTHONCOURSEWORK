# for taking inputs in python we have a method input()

a = input("Enter your age: ")

b = 18
print("python takes inputs as string",type(a))
print("This is type for b",type(b))

# If we want a particular type to be an input

a = float(input("Enter your float:"))
print("this will be float now", type(a))

# Outputs in python we use print()
print("We are learning python")
a = 10
print("The value of a is", a)

# how we format string 
print("the value of a is {} greater than 1".format(a))

# you can also use % as formatting 
'''
%d is for integers(int)
%f is for decimal(float)
%c is for characters
%s is for strings(str)
'''

a = "Harsha"
print("the value of a is %s greater than 1" % a)

# Lets say we have three numbers being date month and year (13,6,2025) - 13-6-2025
print(13,6,2025,sep="-")