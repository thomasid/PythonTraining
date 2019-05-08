# picking random word from a word library in txt file
import random

with open(r"C:\Users\tsida\PycharmProjects\First_Project\sowpods.txt","r") as f:
    line = random.choice(f.readlines())

print(line)