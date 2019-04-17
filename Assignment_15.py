# Write string of words backwards
def user_input(promptText="Input a string of words: "):
    user_input = input(promptText)
    return user_input

def backwards(unser_input):
    split_string = unser_input.split()[::-1]
    split_string = " ".join(split_string)
    return split_string

user_input_string = user_input()
backwards_string = backwards(user_input_string)

print(backwards_string)