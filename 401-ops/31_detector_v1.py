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

# Check if a temp folder exists for the log file.
if not os.path.exists("temp"):
    os.makedirs("temp")

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        logging.FileHandler('temp/file_detector_log.log'),
                       # logging.StreamHandler()
                    ])


def user_input(target):
    try:
        input_value = input(f'Enter {target}: ')
        logging.info(f'User input for {target}: {input_value}')
        return input_value
    except KeyboardInterrupt:
        logging.warning("User initiated exit.")
        exit()


def directory_input():
    while True:
        path_input = user_input("DIRECTORY")
        path = path_check(path_input)
        if os.path.exists(path):
            logging.info(f'Valid directory entered: {path}')
            return path
        logging.error('Directory does not exist: %s', path)
        print("Please enter a valid directory path.")


def path_check(path):
    if path.startswith('~'):
        expanded_path = os.path.expanduser(path)
        logging.info('Directory path expanded from %s to %s', path, expanded_path)
        return expanded_path
    else:
        return path

def search_files(directory, filename):
    '''Search function that works in Windows (tested with Cmder and Alacritty) and Ubuntu'''
    file_count = 0
    files_searched = 0
    print(f'\nSearching for {filename.upper()} in {directory.upper()} directory\n')
    for root, dirs, files in os.walk(directory):
        for file in files:
            files_searched += 1
            if file == filename:
                file_count += 1
                file_path = os.path.join(root, file)
                logging.info(f'Found: {file_path}')
                print(f"Found: {file}")
    logging.info(f"Files searched: {files_searched}, Hits found: {file_count}")
    print(f"\nFiles searched: {files_searched}, Hits found: {file_count}")

def main():
    logging.info("[  =======  File Detection Script Initialized ======= ]")
    print("\n[  =======  File Detection Script ======= ]")
    filename = user_input("FILE NAME")
    directory = directory_input()
    search_files(directory, filename)
    logging.info("[  =======  File Detection Script Completed ======= ]")


if __name__ == "__main__":
    main()
