#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      02/21/2024
#
#
# REQUIREMENTS:
# Successfully connect to the VirusTotal API
# Automatically compare your target file’s md5 hash with the hash values of entries on VirusTotal API
# Print to the screen the number of positives detected and total files scanned

import logging
import os
import hashlib


# Check if a temp folder exists for the log file.
if not os.path.exists("temp"):
    os.makedirs("temp")

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        logging.FileHandler('temp/file_hasher.log'),
                       # logging.StreamHandler()
                    ])

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

def search_files(directory):

    files_searched = 0
    print(f'\nScanning files in {directory.upper()} directory\n')
    for root, dirs, files in os.walk(directory):
        for file in files:
            files_searched += 1
            file_path = os.path.join(root, file)
            logging.info(f'Found: {file_path}')
            print(f"Found: {file}")
    logging.info(f"Files searched: {files_searched}, Hits found: {file_count}")
    print(f"\nFiles searched: {files_searched}, Hits found: {file_count}")

def main():
    logging.info("[  =======  File Detection Script Initialized ======= ]")
    print("\n[  =======  File Detection Script ======= ]")
    directory = directory_input()
    search_files(directory)
    logging.info("[  =======  File Detection Script Completed ======= ]")


if __name__ == "__main__":
    main()
