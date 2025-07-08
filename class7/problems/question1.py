'''
Given an array print all the  even  elements only once even if they are repeating in that array using comprejhension

example : [1,2,3,4,5,1,2,3,4,5]

output: [2,4]

'''
arr = [1,2,3,4,5,1,2,3,4,5]
result = {x for x in arr if x%2==0}
print(result)