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

# import scapy

target = "scanme.nmap.org"
print(f'Default target: {target}')

while True:  # loop for first prompt
    change_target = input("Do you wish to change target [Y/N]: ").lower()

    if change_target == 'y':
        while True:  # loop for entering a new target
            new_target = input("Enter new target: ")
            print(f'New target: {new_target}')
            continue_input = input("Continue with this target? [Y/N] ").lower()

            if continue_input == 'y':
                target = new_target  # update the target variable
                break  # breaks out of the inner loop

        break  # break out of the outer loop

    elif change_target == 'n':
        break

print(f'Current target: {target}')