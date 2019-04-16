# Program prints out all elements of the list that are less than 5
# Ask the user for a number and return a list that contains only elements
# from the original list a that are smaller than that number given by the user.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = [item for item in a if item < 5]
print(num)

innum = int(input("Give a number: "))
input_num = [item for item in a if item < innum]
print(input_num)