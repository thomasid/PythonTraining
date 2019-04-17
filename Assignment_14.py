# Function takes a list and returns a new list without the duplicates
from random import sample

def remove_duplicates(in_list):
    return set(in_list)

def cicle_duplicates(in_list):
    b = []
    for val in in_list:
        if val not in b:
            b.append(val)
    return b

a = [1,1,2,3,4,5,5,6,7,8,8]
b = remove_duplicates(a)
print(b), print(len(b))

c = cicle_duplicates(a)
print(c), print(len(c))