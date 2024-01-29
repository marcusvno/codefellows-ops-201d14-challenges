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

from scapy.all import sr1, IP, TCP, send
import random


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

        elif change_target == 'n':
            print(f'\nCurrent target: {target}')
            return target


def port_range_prompt():
    while True:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        if start_port <= end_port:
            if start_port == end_port:
                confirm = input(f'Scan port {start_port} [Y/N]: ')
            confirm = input(f'Scan ports {start_port}-{end_port} [Y/N]: ')
            if confirm.lower() == 'y':
                return [start_port, end_port]
        elif start_port > end_port:
            print("\nInvalid range. Start port must be less than or equal to end port.\n")


def port_scan(target, port_range):
    choice = input("Do you want to see closed ports [Y/N]: ")
    for port in range(port_range[0], port_range[1]+1):
        response = sr1(IP(dst=target)/TCP(sport=(random.randint(2000, 65000)),dport=port, flags="S"), timeout=2, verbose=0) # Send SYN
        if response is None:
            print(f'{port} sent no response. Filtered?')
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12: # SYN-ACK received. Port open
                send(IP(dst=target)/TCP(sport=(random.randint(2000, 65000)),dport=port, flags="R"), verbose=0) # Sends RST to close connection
                print(f'{port} is open.')
            elif choice.lower() == 'y' and response.getlayer(TCP).flags == 0x14: #RST-ACK received. Port closed
                print(f'{port} is closed.')
        else:
            print(f'{port} sent an unexpected response.')


def main():
    target = target_prompt()
    port_range = port_range_prompt()
    port_scan(target,port_range)


if __name__ == "__main__":
    main()
