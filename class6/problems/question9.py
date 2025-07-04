'''
Given two numbers swap the numbers

x = 1 , y = 0 -> function -> y=1 , x =0 
'''

def swap(x,y):
    return y , x

def swap1(x,y):
    z = x
    x = y
    y = z
    print(f"x : {x}")
    print(f"y: {y}")


x = 1
y = 0
print(f"x : {x}")
print(f"y: {y}")
x , y = swap(x,y)
print(f"x : {x}")
print(f"y: {y}")

swap1(x,y)

