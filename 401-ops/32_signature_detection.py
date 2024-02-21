#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      02/20/2024
#
#
# REQUIREMENTS:
# Alter your search code to recursively scan each file and folder in the user input directory path and print it to the screen.
# For each file scanned within the scope of your search directory:
#   - Generate the file’s MD5 hash using Hashlib.
#   - Assign the MD5 hash to a variable.
#   - Print the variable to the screen along with a timestamp, file name, file size, and complete (not symbolic) file path.

import logging
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        logging.FileHandler('file_detector_log.log'),
                        logging.StreamHandler()
                    ])


def user_input(target):
    try:
        return input(f'Enter {target}: ')
    except KeyboardInterrupt:
        logging.warning("User initiated exit.")
        exit()


def directory_input():
    while True:
        path_input = user_input("DIRECTORY")
        path = path_check(path_input)
        if os.path.exists(path):
            return path
        logging.error(f'Directory does not exist.')
        print("Please enter a valid directory path.")


def path_check(path):
    if path.statswith('~'):
        logging.info('Directory path expanded to %s', os.path.expanduser(path))
        return os.path.expanduser(path)
    else:
        return path


def main():
    print("\n[  =======  File Detection Script ======= ]")
    filename = user_input("FILE NAME")
    directory = directory_input()


if __name__ == "__main__":
    main()
