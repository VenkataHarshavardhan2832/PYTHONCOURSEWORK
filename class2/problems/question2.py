'''
Take a list of integers,
scores = [100, 10, 30, 60, 90,40,60]

append it with 3 more scores and extend it with scores_2 = [70, 80, 50,100]

Now sort the resulting list in descending order and print the sorted list.

and create the list from the resulting list with starting 5 values and remove the last value from the list and first occurence of 100 from the list
'''
scores = [100, 10, 30, 60, 90,40,60]
scores.append(50)
scores.append(80)
scores.append(70)

#extend it with scores_2
scores_2 = [70, 80, 50,100]
scores_2.extend(scores_2)

#The resulting list in descending order
scores.sort(reverse=True)
print(scores)

#create the list from the resulting list with starting 5 values and remove the last value from the list and first occurence of 100 from the list
starting_scores = scores[:5]
scores.pop()
if 100 in starting_scores:
    starting_scores.remove(100)
print(starting_scores)
