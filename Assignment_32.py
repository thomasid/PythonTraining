# Hangman game
import random

def random_word():
    with open(r"C:\Users\tsida\PycharmProjects\First_Project\sowpods.txt","r") as f:
        line = random.choice(f.readlines())
    return line


if __name__ == "__main__":
    print("Welcome to Hangman game!")
    decision = "y"
    while decision == "y":
        word = random_word()
        hiddenWord = ["_" for letter in word.strip()]
        print(" ".join(hiddenWord))
        hangmanWord = [letter for letter in word.strip()]
        guessCounter = 6
        guessedLetters = []
        while "_" in hiddenWord and guessCounter != 0:
            userGuess = input("Guess your letter: ").upper()
            if userGuess not in guessedLetters and userGuess in hangmanWord:
                while userGuess in hangmanWord:
                    hiddenWord[hangmanWord.index(userGuess)] = hangmanWord[hangmanWord.index(userGuess)]
                    hangmanWord[hangmanWord.index(userGuess)] = "0"
                    guessedLetters.append(userGuess)
                print(" ".join(hiddenWord))
                guessCounter -= 1
                print("You have %s guesses left!" % (guessCounter))
            elif userGuess not in hangmanWord and userGuess not in guessedLetters:
                guessCounter -= 1
                print("No such letter in the word!")
                print("You have %s guesses left!" % (guessCounter))
            elif userGuess in guessedLetters:
                print("You already guessed this letter!")
        if "_" not in hiddenWord:
            print("You guessed the word!")
            print("".join(hiddenWord))
        else:
            print("You lost... The word was: %s" % (word))
        decision = input("Play again? (y/n): ")
    print("Bye Bye now!")