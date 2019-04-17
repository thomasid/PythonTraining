# Take a list of numbers and make a new list of only first and last element of the list
from random import sample

a = sample(range(100), 10)
print(a)

b = [a[0], a[len(a)-1]]
print(b)