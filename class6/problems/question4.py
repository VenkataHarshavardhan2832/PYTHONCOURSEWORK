'''
Do all mathematic operations on a set - union,intersection,difference,symettric difference.

CHeck if a set is subset of another set.

Explore about frozen sets in python
'''
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A.union(B))

print(A.intersection(B))
print(B.intersection(A))
print(A - B)
print(B-A)
print(A.symmetric_difference(B))
C = {1, 2}
print(C.issubset(A))
print(A.issuperset(C))
