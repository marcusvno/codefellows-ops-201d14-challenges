# Script Name:                  Directory Creation
# Author:                       Marcus Nogueira
# Date of latest revision:      12/05/1986
# Purpose:                      Python script that generates all directories, sub-directories and files for a user-provided directory path.

# Import Libraries
import os
import time


# Declaration of variables
BLUE = "\033[34m"  # Blue text
GREEN = "\033[32m"  # Green text
YELLOW = "\033[33m"  # Yellow text
RESET = "\033[0m"  # Reset to default color


# Declaration of functions

def banner():
    os.system('clear')
    os.system('figlet "Walk in the Dir Path" -w 300 -f "ANSI Shadow" | lolcat')

def get_filepath():

    while True:
        filepath = str(input("\nEnter ABSOLUTE file path: "))
        print(f'\nSearching for {BLUE}{filepath}{RESET} ')
        time.sleep(0.6)
        if os.path.exists(filepath):
            print(f'{BLUE}{filepath}{RESET} found.')
            time.sleep(1)
            return filepath
        else:
            print(f'The file path {BLUE}{filepath}{RESET} does not exist.')
            time.sleep(1)


def stroll(dirpath):
    dir_count = 0
    file_count = 0

    for (root, dirs, files) in os.walk(dirpath):
        print(f'\nDIRECTORY: {BLUE}{root}{RESET}\n    SUBDIRECTORIES:')
        for subdir in dirs:
            print(f'      {YELLOW}- {subdir}{RESET}')
        print('    FILES:')
        for file in files:
            print(f'      {GREEN}- {file}{RESET}')

        dir_count += len(dirs)
        file_count += len(files)

    print(f'\n{dir_count} directories, {file_count} files')

# main block
if __name__ == "__main__":
    banner()
    USER_INPUT = get_filepath() 
    stroll(USER_INPUT) # challenge requirement to pass filepath to function
