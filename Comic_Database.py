import csv
import re
from typing import List

f = open("Brett_Comic_Dump", "r")


def find_issue():
    issue= input("What issue(s) are you searchin' for? ")
    for row in csv.reader(f, delimiter= ";"):
        if re.search(issue, str(row[0])):
            print(row[0], "issue", row[1])


def find_creator():
    author= input("Who are we searchin' for? ")
    row: List[str]
    for row in csv.reader(f, delimiter= ";"):
        if re.search(author, str(row[5])):
            print("The writer and artist(s) for", row[0] + " is: " + row[5])

def find_publish_date():
    released= input("What year are we searchin' for? ")
    row: List[str]
    for row in csv.reader(f, delimiter= ";"):
        if re.search(released, str(row[4])):
            print(row[0] + row[1], "was published in " + row[4])


def main():
    while True:
        choice= input\
        ("""Welcome to Brett\'s Nerd Collection! What would you like to see?
        Press 1 to search by Issue Name.
        Press 2 to search by Author/Artist(s).
        Press 3 to search by Release Date""")
        if choice == "1":
            find_issue()
        elif choice == "2":
            find_creator()
        elif choice == "3":
            find_publish_date()
        else:
            print("I\'m sorry fellow nerd, please try again!")

        answer = input("Would you like to try again? Y or N?")

        if answer not in ("y", "n"):
            print("Wrong again, geez! Goodbye!")
            break

        if answer == "y":
            continue
        else:
            input("\nExcelsior! Press ENTER to exit")
            break

main()
