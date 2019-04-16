# Generate a random number and user to guess a value
import random
counter=0
decision=0
while 1:
    rnd_num = random.randint(1, 9)
    decision = input("Guess a number between 1 and 9. Type 'exit' if you wish to quit the game: ")
    if decision.lower() == "exit":
        break
    elif int(decision) > rnd_num:
        print("Your guess is too high!")
    elif int(decision) < rnd_num:
        print("Your guess is too low!")
    elif int(decision) == rnd_num:
        print("You guessed the number!")
    counter+=1
print("End of the game. You played %d times" %(counter))
