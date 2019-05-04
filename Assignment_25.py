# Guessing a number game
from random import randint

def user_input(guessNumber):
    myGuess = input("Is your number %s? (Type y for yes, h for too high, l for too low): "%(guessNumber))
    return myGuess

def too_high(cGuess, lNumber):
    newGuess = int(lNumber+((cGuess-lNumber)/2))
    return newGuess

def too_low(cGuess, mNumber):
    newGuess = int(cGuess + ((mNumber - cGuess) / 2))
    return newGuess

if __name__ == "__main__":
    userNumber = int(input("Choose the number from 0 to 100? "))
    guessNumber = randint(1,100)
    maxNumber = 100
    lowNumber = 0
    myGuess = "none"
    guessCounter = 0
    while myGuess != "y":
        myGuess = user_input(guessNumber)
        guessCounter += 1
        if myGuess == "h":
            maxNumber = guessNumber
            guessNumber = too_high(guessNumber, lowNumber)
        elif myGuess == "l":
            lowNumber = guessNumber
            guessNumber = too_low(guessNumber, maxNumber)
    print("I guessed your number! it is %s!" % (guessNumber))
    print("I guessed %s times."% (guessCounter))