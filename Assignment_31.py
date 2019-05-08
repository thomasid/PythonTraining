# picking random word from a word library in txt file
import random

def random_word():
    with open(r"C:\Users\tsida\PycharmProjects\First_Project\sowpods.txt","r") as f:
        line = random.choice(f.readlines())
    return line


if __name__ == "__main__":
    print("Welcome to Hangman game!")
    word = random_word()
    hiddenWord = ["_" for letter in word.strip()]
    print(" ".join(hiddenWord))
    hangmanWord = [letter for letter in word.strip()]
    guessedLetters = []
    while "_" in hiddenWord:
        userGuess = input("Guess your letter: ").upper()
        if userGuess not in guessedLetters and userGuess in hangmanWord:
            while userGuess in hangmanWord:
                hiddenWord[hangmanWord.index(userGuess)] = hangmanWord[hangmanWord.index(userGuess)]
                hangmanWord[hangmanWord.index(userGuess)] = "0"
                guessedLetters.append(userGuess)
            print(" ".join(hiddenWord))
        elif userGuess not in hangmanWord and userGuess not in guessedLetters:
            print("No such letter in the word!")
        elif userGuess in guessedLetters:
            print("You already guessed this letter!")
    print("You guessed the word!")
    print("".join(hiddenWord))