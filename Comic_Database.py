import csv
import re
from typing import List

f = open("Brett_Comic_Dump", "r")


def find_issue():
    issue= input("What we searchin' for? ")
    for row in csv.reader(f, delimiter= ";"):
        if re.search(issue, str(row[0])):
            print(row[0])


def find_creator():
    author= input("Who are we searchin' for? ")
    row: List[str]
    for row in csv.reader(f, delimiter= ";"):
        if re.search(author, str(row[5])):
            print(row[0] + " was written by " + row[5])


def main():
    choice= input("Press 1 to search by issue name. "
                  "Press 2 to search by author.")
    if choice == "1":
        find_issue()
    elif choice == "2":
        find_creator()
main()
