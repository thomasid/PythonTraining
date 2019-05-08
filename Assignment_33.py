# Birthday list

birthdays = {"Tomas": "01/01/1990",
             "Petras": "02/02/1995",
             "Jonas": "03/03/2000"}

if __name__ == "__main__":
    print("Welcome to birthday dictionary! We know following birthdays: ")
    for key in birthdays.keys():
        print(key)
    request = input("Whose birthday would you like to know? ")
    print(birthdays[request])