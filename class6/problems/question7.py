'''
Given an string find the most repeating charecter in the string, if there are multiple then only return the first occuring

example : string = 'harsha'
answer : h 

Write an another function which returns highest repeating and last occuring

example : string = 'harsha'
answer : a
'''
s = 'harsha'
def most_repeating_first(s):
    max_count = 0
    result = ''
    for ch in s:
        count = s.count(ch)
        if count > max_count:
            max_count = count
            result = ch
    return result
print(most_repeating_first(s))

def most_repeating_last(s):
    max_count = 0
    result = ''
    for ch in s:
        count = s.count(ch)
        if count > max_count or (count == max_count and s.rindex(ch) > s.rindex(result)):
            max_count = count
            result = ch
    return result
print(most_repeating_last(s))
