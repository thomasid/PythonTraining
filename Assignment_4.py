# Print a list of divisors of user input number
input_num = int(input("Give a number: "))

new_list = [item for item in range(1,input_num+1) if input_num % item == 0]
print(new_list)