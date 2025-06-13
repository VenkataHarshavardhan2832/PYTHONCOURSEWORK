import keyword

age = int(input("Enter your age:"))
name = input("Enter your name")
# Whenever you use operators like + , - , = or any other operator keep a space before and after the operator

# Naming variable styles
# 1. snake_case - all lowercase letters with underscores between words (harshas_age)
# 2. camelCase - first letter of each word is capitalized except the first word (harshasAge)
# 3. PascalCase - first letter of each word is capitalized (HarshasAge)

# keywords in python - keywords are reserved words in python which cannot be used as variable names

# if = 10 this is wrong
print("Keywords in python are:",keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''


a = 100

print(a)

del a  # this will delete the variable a

#print(a) # this will give an error because a is deleted