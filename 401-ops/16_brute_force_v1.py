#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      01/29/2024
#
# Purpose: Build an automated brute force wordlist
#
# REQUIREMENTS:
# Create a script that prompts the user to select one of the following modes:
#   Mode 1: Offensive; Dictionary Iterator
#       - Accepts a user input word list file path and iterates through the word list, assigning the word being read to a variable.
#       - Add a delay between words.
#       - Print to the screen the value of the variable.
#   Mode 2: Defensive; Password Recognized
#       - Accepts a user input string.
#       - Accepts a user input word list file path.
#       - Search the word list for the user input string.
#       - Print to the screen whether the string appeared in the word list.
#
# REFERENCE:
# For the Password Complexity Test: https://www.w3schools.com/python/python_ref_string.asp

from time import sleep
import os


def menu():
    while True:
        print("\n---------------------------")
        print("|        Robot Hulk       |")
        print("---------------------------")
        print("| 1. Dictionary Iterator  |")
        print("| 2. Search for Word      |")
        print("| 3. Password Test        |")
        print("| Q. Quit                 |")
        print("---------------------------")
        choice = input(" Enter menu option: ")
        if choice in ["1", "2", "3"]:
            print()
            return choice
        elif choice.lower() == "q":
            exit()
        else:
            print("Invalid choice. Please choose another option.")
            sleep(.5)


def load_file():
    file_path = file_path_input()
    file_name = os.path.basename(file_path)
    password_list = []
    print(f"\nPRINTING {file_name}\n")
    with open(file_path, 'r') as file:
        for line in file:
            password_list.append(line.strip())
            print(line.strip())
            sleep(.3)


def password_search():
    word = input("Enter word: ")
    file_path = file_path_input()
    file_name = os.path.basename(file_path)
    password_list = []
    print(f'\nSEARCHING {file_name} for "{word}"')
    with open(file_path, 'r') as file:
        for line in file:
            password_list.append(line.strip())

    if word in password_list:
        print(f'"{word}" found.')
    else:
        print(f'"{word}" not found.')


def file_path_input():
    file_path = input("Enter file path to dictionary: ")
    return file_path


def password_complexity():
    print("\n-------------------------------------------")
    print("|               Password Test             |")
    print("-------------------------------------------")
    print("| 1. Must use at least 8 characters       |")
    print("| 2. Must use at least 2 capital letters  |")
    print("| 3. Must use at least 2 numbers          |")
    print("| 4. Must use at least 2 symbols          |")
    print("-------------------------------------------")
    while True:
        password = input(" Enter password to test: ")
        uppercase_count = check_caps(password)
        num_count = check_nums(password)
        sym_count = check_sym(password)
        print()
        if len(password) >= 8:
            print("Passed LENGTH requirement.")
            sleep(.3)
            if uppercase_count >= 2:
                print("Passed UPPERCASE requirement.")
                sleep(.3)
                if num_count >= 2:
                    print("Passed NUMBERS requirement.")
                    sleep(.3)
                    if sym_count >= 2:
                        print("Passed SYMBOLS requirement.")
                        sleep(.3)
                        print('\nPASSED TEST.')
                        break
                    else:
                        print("Failed SYMBOLS test. Use more SYMBOLS.\n")
                else:
                    print("Failed NUMBERS test. Use more NUMBERS.\n")
            else:
                print("Failed UPPERCASE TEST. Use more UPPERCASE letters.\n")
        else:
            print("Password NOT long enough.\n")


def check_caps(password):
    upper = 0
    for char in password:
        if char.isupper():
            upper += 1

    return upper


def check_nums(password):
    num = 0
    for char in password:
        if char.isnumeric():
            num += 1
    return num


def check_sym(password):
    sym = 0
    for char in password:
        if not char.isalnum():
            sym += 1
    return sym


if __name__ == "__main__":
    choice = menu()
    match choice:
        case "1": load_file()
        case "2": password_search()
        case "3": password_complexity()
