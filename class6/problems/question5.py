'''
Given an array find the most repeating element in the array.

example:
Input : [1,2,3,4,1,1,1,2,3,4]
answer : 1
'''
def most_repeating_element(arr): # user defined
    count_dict={}
    for number in arr:
        if number in count_dict.keys():
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    '''
    {
        1 : 2,
        3 : 4,
        2 : 2,
        4 : 2
    }
    '''

    repeat = 0
    answer = 0
    for key, value in count_dict.items(): # these are inbuilt functions
        if value > repeat:
            repeat = value # repeat = 4
            answer = key # answer = 3
    return answer
ans = most_repeating_element(arr=[1,2,3,4,3,1,3,2,3,4])
print(ans)