# This program checks if the input number is odd or even, if it is multiple of 4
num = int(input("Give a number: "))
check = int(input("Give a number to divide by: "))

if num / 4 == 1:
    print("Your input number is a multiple of 4")
elif num % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd")

if num % check == 0:
    print("Your number is divided evenly")
else:
    print("Your number is not divided evenly, remainder: " + str(num%check))