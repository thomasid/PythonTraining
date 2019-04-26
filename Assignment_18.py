# Cow and bull game
from random import randint

def random_number():
    return randint(1000,9999)

def number_compare(random_number,player_guess):
    cows = 0
    bulls = 0
    for i in range(0, len(player_guess)):
        if player_guess[i] == random_number[i]:
            cows+=1
        else:
            bulls+=1
    return cows, bulls


if __name__ == "__main__":
    guess_no = 0
    right_guess = 0
    while right_guess==0:
        guess_no+=1
        rand_num = str(random_number())
        rand_num="1234"
        player_guess = input("Please input your guess (4dgit number): ")
        print("Random number: ",rand_num)
        cows, bulls=  number_compare(rand_num, player_guess)
        if cows == 4:
            print("Congratulations, you win - you got 4 cows! You guessed %s times"%(guess_no))
            right_guess = 1
        else:
            print("You got %s cows and %s bulls. You guessed %s times" %(cows,bulls,guess_no))