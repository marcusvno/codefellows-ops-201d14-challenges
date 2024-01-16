# Author:                       Marcus Nogueira
# Date of latest revision:      01/16/2024
#
# OBJECTIVE: Python script that uses a cryptography library to:
#   - Encrypt a File
#   - Decrypt a File
#   - Encrypt a Message
#   - Decrypt a Message
# Use a menu for the above and then depending on the selection, prompt for more info.
#
# REQUIRED PACKAGES:
# pip install cryptography
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


# def write_key():
#     '''Generates a new key and writes it to a file.'''
#     key = Fernet.generate_key()  # Generate the key
#     script_dir = os.path.dirname(__file__)  # Get the directory of the script
#     key_path = os.path.join(script_dir, "key.key")  # Path to the key file
#     with open(key_path, "wb") as key_file:
#         key_file.write(key)


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
        print("  | 3. Encrypt a Message     |")
        print("  | 4. Decrypt a Message     |")
        print("  | 5. Quit                  |")
        print("  ----------------------------")
        choice = input("  Select one of the above: ")

        if choice in ["1", "2", "3", "4",]:
            print()
            return choice
        elif choice == "5":
            exit()
        else:
            print("Invalid choice. Please choose a valid number.")
            time.sleep(.5)
            os.system('clear')


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
            file.write(encrypted_data) # overwrites the file with decrypted data
        print(f'{filepath} has been encrypted.')
    elif mode == 'DECRYPT':
        with open(filepath, "rb") as file:
            encrypted_data = file.read()  # reads encrypted file

        decrypted_data = f.decrypt(encrypted_data)  # decrypts the data

        with open(filepath, "wb") as file:
            file.write(decrypted_data) # overwrites the file with decrypted data
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
            case "3": message_prompt('ENCRYPT')
            case "4": message_prompt('DECRYPT')
        script_quit()
