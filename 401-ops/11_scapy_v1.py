#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      01/22/2024
#
# Purpose: Build our own network scanning tool with scapy.
#
# REQUIREMENTS:
# In Python, create a TCP Port Range Scanner that tests whether a TCP port is open or closed. The script must:
#
# Utilize the scapy library
#   - Define host IP
#   - Define port range or specific set of ports to scan
#   - Test each port in the specified range using a for loop
#   - If flag 0x12 received, send a RST packet to graciously close the open connection. Notify the user the port is open.
#   - If flag 0x14 received, notify user the port is closed.
#   - If no flag is received, notify the user the port is filtered and silently dropped.

from scapy.all import sr1, IP, ICMP

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


def main():
    menu_choice = menu()
    target = target_prompt()
    range = port_range()
    print(range)


if __name__ == "__main__":
    main()
