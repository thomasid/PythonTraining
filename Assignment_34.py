# Birthday list
import json

with open(r"C:\Users\tsida\PycharmProjects\First_Project\info.json", "r") as f:
    birthdayLibrary = json.load(f)

if __name__ == "__main__":
    print("Welcome to birthday dictionary! We know following birthdays: ")
    for key in birthdayLibrary.keys():
        print(key)
    request = input("Whose birthday would you like to know? ")
    print("{} birthday is on {}".format(request,birthdayLibrary[request]))
    newBirthday = input("Would you like to add another birthday? (y/n): ")
    if newBirthday == "y":
        name = input("Write down a name: ")
        birthday = input("Write down a birthday mm/dd/yyyy: ")
        birthdayLibrary.update({name:birthday})
        with open(r"C:\Users\tsida\PycharmProjects\First_Project\info.json", "w") as f:
            birthdayLibrary = json.dump(birthdayLibrary, f)