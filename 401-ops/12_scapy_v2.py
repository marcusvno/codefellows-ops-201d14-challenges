#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      01/22/2024
#
# Purpose: Build our own network scanning tool with scapy.
#
# REQUIREMENTS:
# Add the following features to your Network Security Tool:
# User menu prompting choice between TCP Port Range Scanner mode and ICMP Ping Sweep mode, with the former leading to yesterday’s feature set
#   - ICMP Ping Sweep tool
#       - Prompt user for network address including CIDR block, for example “10.10.0.0/24”
#       (Careful not to populate the host bits!)
#
#   - Create a list of all addresses in the given network
#   - Ping all addresses on the given network except for network address and broadcast address
#       - If no response, inform the user that the host is down or unresponsive.
#       - If ICMP type is 3 and ICMP code is either 1, 2, 3, 9, 10, or 13 then inform the user that the host is actively blocking ICMP traffic.
#       - Otherwise, inform the user that the host is responding.
#   - Count how many hosts are online and inform the user.

from time import sleep
import ipaddress
from scapy.all import sr1, IP, ICMP


def menu():
    '''Present user with options for encryption/decryption'''
    print()
    while True:
        print("  -------------------------")
        print("  | 1. Port Scanner       |")
        print("  | 2. ICMP Ping Sweep    |")
        print("  | 3. Quit               |")
        print("  -------------------------")
        choice = input("  Select one of the above: ")

        if choice in ["1", "2", "3"]:
            print()
            return choice
        elif choice == "3":
            exit()
        else:
            print("Invalid choice. Please choose a valid number.")
            sleep(.5)


def target_prompt():
    target = "scanme.nmap.org"
    print(f'\nDefault target: {target}')
    while True:  # loop for first prompt
        change_target = input("Do you wish to change target [Y/N]: ").lower()

        if change_target == 'y':
            while True:  # loop for entering a new target
                new_target = input("Enter new target: ")
                print(f'New target: {new_target}')
                continue_input = input(
                    "Continue with this target? [Y/N] ").lower()

                if continue_input.lower() == 'y':
                    target = new_target  # update the target variable
                    print(f'\nCurrent target: {target}')
                    return target  # breaks out of the inner loop

            # break  # break out of the outer loop

        elif change_target == 'n':
            print(f'\nCurrent target: {target}')
            return target


def port_range():
    while True:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        if start_port == end_port:
            confirm = input(F'Scan port {start_port} [Y/N]: ')
            if confirm.lower() == 'y':
                return [start_port, end_port]
        elif start_port < end_port:
            confirm = input(F'Scan ports {start_port}-{end_port} [Y/N]: ')
            if confirm.lower() == 'y':
                return [start_port, end_port]
        elif start_port > end_port:
            print("\nInvalid range.\n")


def network_prompt():
    while True:
        user_input = input("\nEnter target network IPv4 CIDR: ")
        if ipaddress.IPv4Address(user_input).is_global is True:
            confirm = input(f'{user_input} is a public network. Continue? [y/n] ')
            if confirm.lower() == 'y':
                    sweeper(user_input)
        if ipaddress.IPv4Address(user_input).is_private is True:
            confirm = input(f'{user_input} is a private network. Continue? [y/n] ')
            if confirm.lower() == 'y':
                    sweeper(user_input)
        
        

def sweeper()

def main():
    menu_choice = menu()
    match menu_choice:  # Follow up prompt based on menu choice
        case "1":
            target = target_prompt()
            range = port_range()
        case "2": network_prompt()


if __name__ == "__main__":
    main()
