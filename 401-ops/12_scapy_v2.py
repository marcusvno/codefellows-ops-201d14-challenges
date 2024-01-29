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
#
# TO USE THE SCRIPT:
#   - Install scapy with sudo because it needs elevated privileges to create packets at the Network (layer 3) level.
#        - sudo pip3 install scapy
#   - To run the script, use sudo for the reason above.
#       - sudo python3 12_scapy_v2.py
#


from time import sleep
import ipaddress
import logging
from scapy.all import sr1, IP, TCP, send, ICMP, conf
import random

# Silences a MAC Address warning that I was getting from IPs not assigned to anything.
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

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


def network_prompt():
    while True:
        user_input = input("\nEnter target network IPv4 CIDR: ")
        if ipaddress.IPv4Network(user_input).is_global is True:
            confirm = input(
                f'{user_input} is a public network. Continue? [y/n] ')
            if confirm.lower() == 'y':
                return user_input
        if ipaddress.IPv4Network(user_input).is_private is True:
            confirm = input(
                f'{user_input} is a private network. Continue? [y/n] ')
            if confirm.lower() == 'y':
                return user_input


def sweeper(target_network):
    ip_list = ipaddress.IPv4Network(target_network).hosts()
    choice = input("\nDo you want to see offline or unresponsive hosts [Y/N]: ")

    print(f'\nScanning {target_network}...')
    host_count = 0
   
    for host in ip_list:
        res = sr1(IP(dst=str(host))/ICMP(), timeout=2, verbose=0)
        if res is None:
            if choice.lower() == 'y':
                print(f'{host} is down or unresponsive.')
        elif res and res.haslayer(ICMP) and res.getlayer(ICMP).type == 3 and res.getlayer(ICMP).code in [1,2,3,9,10,13]:
            print(f'{host} is blocking ICMP traffic.')
            host_count += 1
        else:
            print(f'{host} is responding.')
            host_count += 1
    
    print(f'\nTotal hosts online: {host_count}')


def main():
    menu_choice = menu()
    match menu_choice:  # Follow up prompt based on menu choice
        case "1":
            target = target_prompt()
            port_range = port_range_prompt()
            port_scan(target, port_range)
        case "2": 
            target_network = network_prompt()
            sweeper(target_network)


if __name__ == "__main__":
    main()
