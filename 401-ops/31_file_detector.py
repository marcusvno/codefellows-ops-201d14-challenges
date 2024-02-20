#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      02/19/2024
#
#
# REQUIREMENTS:
#   - Prompt the user to type in a file name to search for.
#   - Prompt the user for a directory to search in.
#   - Search each file in the directory by name.
#       TIP: You may need to perform different commands depending on what OS you’re executing the script on.
#   - For each positive detection, print to the screen the file name and location.
#   - # At the end of the search process, print to the screen how many files were searched and how many hits were found.
#
#   - The script must successfully execute on both Linux and Windows.

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
        return os.path.expanduser(path)
    else:
        return path


def main():
    print("\n[  =======  File Detection Script ======= ]")
    filename = user_input("FILE NAME")
    directory = directory_input()


if __name__ == "__main__":
    main()
