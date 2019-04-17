# Create Fibonnaci sequence of the length defined by user
def user_input(promptText="How many Fibonnaci numbers to generate?: "):
    user_in = int(input(promptText))
    return user_in
fibSeq=[1]
user_value = user_input()
if user_value == 1:
    print(fibSeq)
elif user_value == 2:
    print(fibSeq.append(1))
else:
    fibSeq.append(1)
    for n in range(3,user_value+1):
        new_val = fibSeq[(n-2)]+fibSeq[(n-3)]
        fibSeq.append(new_val)
print(fibSeq)