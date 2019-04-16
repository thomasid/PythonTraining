# This program tells you in what year you will be 100 years of age
import datetime

name = input("Give your name: ")

age = int(input("Give your age: "))

now = datetime.datetime.now()
current_year = now.year

hundred_years = current_year + (100 - age)

print(name + "You will be 100 years in the year of " + str(hundred_years))