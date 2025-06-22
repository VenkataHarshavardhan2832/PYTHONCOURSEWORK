# Function(Functional programing) or Method(Object Oriented Programming)

# Pyton both functional and object oriented, java completely object oriented, c completely functional

# What is a function ? f(x) -> output (one to many mapping in maths) it helps in writing clean code.


# write a function which takes an list as input and gives back sum of all elements as output

# f(list) -> sum of all elements

# function definition
# def funcion_name(a1,a2,a3............)# parameters
# whatever function takes as an input we call it parameter
# Dry - Dont repeat yourself

def sum_of_elements(list_of_elements : list):
    print("We are in the function")
    sum = 0
    for i in list_of_elements:
        sum += i
    return sum
# to run the above function you need to call it

sum = sum_of_elements([1,2,3,4,5]) # fucntion call - whatever you pass to the function here you all it a argument
print(sum)



# you can also write functions that takes nothing and returns nothing

# write a function that prints harshas name

def print_harshas_name():
    print("Harsha!")

print_harshas_name()

# print_harshas_name(1)
