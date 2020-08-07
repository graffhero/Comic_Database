import csv
import re
from typing import List

#f = open("Brett_Comic_Dump", "r")
#comic_lines= csv.reader(f, delimiter= ";")

def find_issue():
    issue= input("What issue(s) are you searchin' for? ")
    f = open("Brett_Comic_Dump", "r")
    comic_lines = csv.reader(f, delimiter=";")
    for row in comic_lines:
        if re.search(issue, str(row[0])):
            print(row[0], "issue", row[1])
    f.close()

def find_creator():
    author= input("Who are we searchin' for? ")
    f = open("Brett_Comic_Dump", "r")
    comic_lines = csv.reader(f, delimiter=";")
    for row in comic_lines:
        if re.search(author, str(row[5])):
            print("The writer and artist(s) for", row[0] + " is: " + row[5])
    f.close()

def find_publish_date():
    released= input("What year are we searchin' for? ")
    f = open("Brett_Comic_Dump", "r")
    comic_lines = csv.reader(f, delimiter=";")
    for row in comic_lines:
        if re.search(released, str(row[4])):
            print(row[0] + row[1], "was published in " + row[4])
    f.close()

def find_issue_number():
    number = input("What issue number are we searchin' for? ")
    f = open("Brett_Comic_Dump", "r")
    comic_lines = csv.reader(f, delimiter=";")
    for row in comic_lines:
        if re.search(number, str(row[1])):
            print("Issue", row[1], row[0])
    f.close()

def find_publisher():
    printed_by = input("Which publisher are we searchin' for? Marvel, DC, Dark Horse, etc.")
    f = open("Brett_Comic_Dump", "r")
    comic_lines = csv.reader(f, delimiter=";")
    for row in comic_lines:
        if re.search(printed_by, str(row[3])):
            print("Publisher", row[3], row[0])
    f.close()

def find_extended_list():
    title_all_info = input("Which issues or series are we searchin' for?")
    f = open("Brett_Comic_Dump", "r")
    comic_lines = csv.reader(f, delimiter=";")
    for row in comic_lines:
        if re.search(title_all_info, str(row[0])):
            print(row[0], "issue number", row[1], "issue title:", row[2], "printed by:", row[3], "on", row[4],
                  "and writen and drawn by", row[5])
    f.close()



def main():
    while True:
        choice= input\
        ("""Welcome to Brett\'s Nerd Collection! What would you like to see?
        Press 1 to search by Issue Name.
        Press 2 to search by Author/Artist(s).
        Press 3 to search by Release Date.
        Press 4 to search by Issue Number.
        Press 5 to search by Publisher.
        Press 6 to search by Issue Name and ALL Information.""")

        if choice == "1":
            find_issue()
        elif choice == "2":
            find_creator()
        elif choice == "3":
            find_publish_date()
        elif choice == "4":
            find_issue_number()
        elif choice == "5":
            find_publisher()
        elif choice == "6":
            find_extended_list()
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
