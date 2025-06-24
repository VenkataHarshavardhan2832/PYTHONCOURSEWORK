'''
Take input from the user for a list of integers, and another integer elemet

print true if element is present in the list, otherwise print false.

example:
list= [1, 2, 3, 4, 5]
element = 3
output: true

list = [10, 20, 30, 40, 50]
element = 60
output: false

'''
list_of_numbers = [1, 2, 3, 4, 5]
element = int(input("Enter a number: "))

def check_element(array, element):
    for i in array:
        if i == element:
            return True
    return False
print(check_element(list_of_numbers, element))