# Make a new list with only even elements
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [val for val in a if val % 2 == 0]
print(b)