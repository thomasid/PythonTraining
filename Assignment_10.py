# Generate random lists, make a new list with common values
from random import sample

a = sample(range(100), 10)
b = sample(range(100), 9)
print(a)
print(b)

new_list = set([val for val in a if val in b])

print(new_list)