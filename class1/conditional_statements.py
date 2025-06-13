# conditional statements executes it part of code based on a condition (if,else ,elif)

# Write a program that takes age as input and tells you are an adult or not

age = int(input("Enter your age: "))

if age >= 18: # if always takes boolean as condition -> relational operators return boolean values
    print("You are an adult")
else: # else is executed when the condition is false(ifs condition is false)
    print("You are not an adult")

# write a program that takes aage as input and tells you are minor adult or senior citizen

a = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
else:
    if age < 60:
        print("You are an adult")
    else:
        print("You are a senior citizen")


# clean way of writing code
if age < 18:
    print("You are a minor")
elif age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")




