'''
Take a string as input form the user print number of times each charecter is repeating

example : harsha
output: h : 2, a:2,r:1,s:1
'''
s = input("Enter a string: ")
for ch in s:
    if s.index(ch) == s.find(ch):  # to avoid printing duplicates
        print(ch, ":", s.count(ch), end=", ")


dictionary = {}
for ch in s:
    if ch in dictionary.keys():
        dictionary[ch] += 1
    else:
        dictionary[ch] = 1
print(dictionary)