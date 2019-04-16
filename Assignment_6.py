# Define if user input string is palindrome
user_string = input("Input String: ")

if user_string.lower() == user_string[::-1].lower():
    print("String is palindrome")
else:
    print("String is not palindrome")