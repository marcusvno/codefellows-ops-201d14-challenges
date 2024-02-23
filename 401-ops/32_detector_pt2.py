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
import hashlib
from datetime import datetime


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

def scan_files(directory):
    print(f'\nScanning files in {directory}\n')
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            md5_hash = hash_file(file_path)
            file_size = os.path.getsize(file_path)
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            logging.debug(f"Hashed: {file_path}, MD5: {md5_hash}")
            print(f'[*] Timestamp: {timestamp} | File: {file_path} | Size: {file_size} bytes | MD5: {md5_hash}')
            

def hash_file(file_path):
    md5_hash = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                md5_hash.update(byte_block)
        return md5_hash.hexdigest()
    except Exception as e:
        logging.error(f"Error generating MD5 for {file_path}: {e}")
        exit()

def main():
    logging.info("[  =======  File Hashing Script Initialized ======= ]")
    print("\n[  =======  File Detection Script ======= ]")
    directory = directory_input()
    scan_files(directory)
    logging.info("[  =======  File Hashing Script Completed ======= ]")


if __name__ == "__main__":
    main()
