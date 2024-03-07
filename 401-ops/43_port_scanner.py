#!/usr/bin/python3

# Author:      Marcus Nogueira
# Description: Port scanner in python
# Date:        03/06/2024

# https://docs.python.org/3/library/socket.html

import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TIMEOUT = 10
sockmod.settimeout(TIMEOUT)

hostip = input("Enter host IPv4: ")
portno = int(input("Enter port :"))

def portScanner():
    if sockmod.connect_ex((hostip, portno)) != 0:
        print("Port closed")
    else:
        print("Port open")

portScanner()