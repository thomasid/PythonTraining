# password generator
import random

numbers = "123456789"
ascii = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "~!@#$%^&*"
randomLetters = []
randomSymbols = []
randomNumbers = []
count=0
while count<5:
    randomLetters.append(ascii[random.randint(1,len(ascii)-1)])
    randomSymbols.append(symbols[random.randint(1,len(symbols)-1)])
    randomSymbols.append(numbers[random.randint(1, len(symbols) - 1)])
    count+=1

genPassword = randomNumbers + randomLetters + randomSymbols
random.shuffle(genPassword)
genPassword = "".join((genPassword))
print(genPassword)