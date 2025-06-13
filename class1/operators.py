# Arthimatic operators for the calculator (+, -, *, /, //, %, **)
# Relational operators for the checking relationship between two values (==, !=, >, <, >=, <=)
# Logical operators for logical operations (and, or, not)
# Assignment operators for assigning values to variables (=, +=, -=, *=, /=, //=, %=, **=)
# Bitwise operators for bitwise(binary) operations (&, |, ^, ~, <<, >>)

a , b = input("Enter two numbers: ").split() # split method will split the input into two parts based on space
a , b = int(a), int(b)  # converting the input to integers

addition = a + a + a + a
subtraction = a - b

print("Addition:", addition)
print("Subtraction:", subtraction)

print(a == b) # reltation operators always returns boolean values
print(a != b)
print(a >= b)
print(a < b)

c = True

a += b # this is same as a = a + b
a -= b # this is same as a = a - b
a *= b # this is same as a = a * b