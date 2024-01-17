# Author:                       Marcus Nogueira
# Date of latest revision:      01/17/2024
#
# Continuation of 06_file_encrypt_pt1.py
#
# OBJECTIVE:
# Add a feature capability to your script to:
#   - Recursively encrypt a single folder and all its contents.
#   - Recursively decrypt a single folder that was encrypted by this tool.
#
# RESOURCES USED:
# https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# https://github.com/codefellows/seattle-cybersecurity-401d10/blob/main/class-06/challenges/DEMO.md

import time  # For ensuring users see a message before the screen changes.
import os  # Used to check if file paths exist
# Used to generate keys and encrypt/decrypt things
from cryptography.fernet import Fernet


def key_check():
    '''Checks if key file exists in the script directory and if not creates one'''
    script_dir = os.path.dirname(__file__)  # Get the directory of the script
    key_path = os.path.join(script_dir, "key.key")  # Path to the key file

    if not os.path.exists(key_path):  # Check if the key file does not exist
        print("Key file not found. Generating new key.")
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        time.sleep(.5)
    else:
        print("Key file found.")
        time.sleep(.5)


def load_key():
    '''Loads key from current directory named "key.key" '''
    script_dir = os.path.dirname(__file__)  # Get the directory of the script
    key_path = os.path.join(script_dir, "key.key")  # Path to the key file
    return open(key_path, "rb").read()


def locksmith_menu():
    '''Present user with options for encryption/decryption'''
    print()
    while True:
        print("  ----------------------------")
        print("  |         Locksmith        |")
        print("  ----------------------------")
        print("  | 1. Encrypt a File        |")
        print("  | 2. Decrypt a File        |")
        print("  | 3. Encrypt a Folder      |")
        print("  | 4. Decrypt a Folder      |")
        print("  | 5. Encrypt a Message     |")
        print("  | 6. Decrypt a Message     |")
        print("  | Q. Quit                  |")
        print("  ----------------------------")
        choice = input("  Select one of the above: ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            print()
            return choice
        elif choice.upper() == "Q":
            exit()
        else:
            print("Invalid choice. Please choose a valid option.")
            time.sleep(.5)


def folder_prompt(mode):
    '''Prompts user for which file to en/decrypt'''
    key = load_key()  # Load previous key
    f = Fernet(key)  # Initialize Fernet module with key

    print(f'{mode} Folder')
    while True:
        folder_path = input('Enter folder name or path: ')
        if os.path.exists(folder_path):
            print("File found.")
            break
        print('File not found.')

    if mode == 'ENCRYPT':
        for root, files in os.walk(folder_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as file:
                    file_data = file.read()  # reads file data

                encrypted_data = f.encrypt(file_data)  # encrypt data

                with open(file_path, "wb") as file:
                    # overwrites the file with decrypted data
                    file.write(encrypted_data)
                print(f'{folder_path} has been encrypted.')
    elif mode == 'DECRYPT':
        for root, files in os.walk(folder_path, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as file:
                    encrypted_data = file.read()  # reads encrypted file

                decrypted_data = f.decrypt(encrypted_data)  # decrypts the data

                with open(file_path, "wb") as file:
                    # overwrites the file with decrypted data
                    file.write(decrypted_data)
                print(f'{folder_path} has been decrypted.')


def file_prompt(mode):
    '''Prompts user for which file to en/decrypt'''
    key = load_key()  # Load previous key
    f = Fernet(key)  # Initialize Fernet module with key

    print(f'{mode} File')
    while True:
        filepath = input('Enter file name or path: ')
        if os.path.exists(filepath):
            print("File found.")
            break
        print('File not found.')

    if mode == 'ENCRYPT':
        with open(filepath, "rb") as file:
            file_data = file.read()  # reads file data

        encrypted_data = f.encrypt(file_data)  # encrypt data

        with open(filepath, "wb") as file:
            # overwrites the file with decrypted data
            file.write(encrypted_data)
        print(f'{filepath} has been encrypted.')
    elif mode == 'DECRYPT':
        with open(filepath, "rb") as file:
            encrypted_data = file.read()  # reads encrypted file

        decrypted_data = f.decrypt(encrypted_data)  # decrypts the data

        with open(filepath, "wb") as file:
            # overwrites the file with decrypted data
            file.write(decrypted_data)
        print(f'{filepath} has been decrypted.')


def message_prompt(mode):
    '''Prompts user for message to en/decrypt'''
    key = load_key()  # Load previous key
    f = Fernet(key)  # Initialize Fernet module with key

    print(f'{mode} Message')

    message = input('Enter message : ').encode()

    if mode == "ENCRYPT":
        # First encodes the message string into bytes and then encrypts it.
        encrypted_message = f.encrypt(message)
        print("\nENCRYPTED MESSAGE:")
        # Print the byte string directly
        print(f'{encrypted_message.decode()}\n')
    elif mode == 'DECRYPT':
        decrypted_message = f.decrypt(message)
        print("\nDECRYPTED MESSAGE:")
        # Decode the byte string to print it
        print(f'{decrypted_message.decode()}\n')


def script_quit():
    '''Checks if the user wishes to continue using the script or quit out.'''
    print()
    if input("Quit? [Y/N]: ").lower() == 'y':
        exit()


if __name__ == "__main__":
    print()
    key_check()

    while True:
        user_input = locksmith_menu()  # Present user with menu
        match user_input:  # Follow up prompt based on menu choice
            case "1": file_prompt('ENCRYPT')
            case "2": file_prompt('DECRYPT')
            case "3": folder_prompt('ENCRYPT')
            case "4": folder_prompt('DECRYPT')
            case "5": message_prompt('ENCRYPT')
            case "6": message_prompt('DECRYPT')
        script_quit()
