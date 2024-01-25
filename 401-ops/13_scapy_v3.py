#!/bin/bash/env python3

# Author:                       Marcus Nogueira
# Date of latest revision:      01/22/2024
#
# Purpose: Build our own network scanning tool with scapy.
#
# REQUIREMENTS:
# Final evolution of this tool
#   - Ping an IP address determined by the user.
#   - If the host exists, scan its ports and determine if any are open.

# from time import sleep
import ipaddress
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

        elif change_target == 'n':
            print(f'\nCurrent target: {target}')
            return target


def ping_check(target):
    p = sr1(IP(dst=target)/ICMP())
    if p:
        print(f'{target} is online.')
        return True
    else:
        print(f'{target} is down or not responding to IMCP.')
        return False


def port_range_prompt():
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


def sweeper(target):
    open_ports = []
    ip = ipaddress.IPv4Address(user_ip)
    print(f'Scanning {target}')

    return open_ports


def main():
    target = target_prompt()
    if ping_check(target):
        open_ports = sweeper(target)
        port_range = port_range_prompt
        if open_ports:
            print(f'Open ports on {target}: {open_ports}')
        else:
            print(f'No open ports found on {target}')


if __name__ == "__main__":
    main()
