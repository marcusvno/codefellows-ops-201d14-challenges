#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      02/21/2024
#
#
# REQUIREMENTS:
# Successfully connect to the VirusTotal API
# Automatically compare your target file’s md5 hash with the hash values of entries on VirusTotal API
# Print to the screen the number of positives detected and total files scanned
#
#
# PREREQS:
# python-dotenv is required to pull our API key from our virustotal.env file
# Download this virtustotal-search.py and rename it 33_virustotal-search-py
# https://raw.githubusercontent.com/eduardxyz/virustotal-search/master/virustotal-search.py

import logging
import os
import hashlib
from datetime import datetime
from dotenv import load_dotenv  # Loads in our environment variables

dotenv_path = 'virustotal.env'

# Check if a temp folder exists for the log file.
if not os.path.exists("temp"):
    os.makedirs("temp")

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        logging.FileHandler('temp/virus_total_scan.log'),
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
        logging.info('Directory path expanded from %s to %s',
                     path, expanded_path)
        return expanded_path
    else:
        return path


def virus_scan_file(directory, filename):
    load_dotenv(dotenv_path=dotenv_path)  # Load in environment variables
    virustotal_api_key = os.getenv('API_KEY_VIRUSTOTAL')
    file_path = os.path.join(directory, filename)

    print(f'\n[*] Hashing {file_path}')

    md5_hash = hash_file(file_path)
    logging.debug(f"Hashed: {file_path}, MD5: {md5_hash}")
    print(f"[*] Hashed: {file_path}, MD5: {md5_hash}")

    query = f'python3 33_virustotal-search.py --md5 {md5_hash} --key {virustotal_api_key}'
    print(f"\n[***] Virus Total Result [***]")
    os.system(query)
    


def hash_file(file_path):
    md5_hash = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
        return md5_hash.hexdigest()
    except Exception as e:
        logging.error(f"Error generating MD5 for {file_path}: {e}")
        exit()


def main():
    logging.info("[  =======  Virus Total Scan Initialized ======= ]")
    print("\n[  =======  Virus Total Scan Initialized ======= ]")
    filename = user_input("FILE NAME")
    directory = directory_input()
    virus_scan_file(directory, filename)
    logging.info("[  =======  Virus Total Scan Complete ======= ]")


if __name__ == "__main__":
    main()
