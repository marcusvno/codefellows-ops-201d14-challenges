'''
This is an Uptime Sensor Tool using ICMP packet pings and Python to determine if hosts on a LAN are up or down. 

REQUIREMENTS:
  - Transmit a single ICMP (ping) packet to a specific IP every two seconds.
  - Evaluate the response as either success or failure.
  - Assign success or failure to a status variable.
  - For every ICMP transmission attempted, print the status variable along with a comprehensive timestamp and destination IP tested.
  
  Example output: 
    2020-10-05 17:57:57.510261 Network Active to 8.8.8.8

RESOURCES: 
https://github.com/alessandromaggio/pythonping
https://web.archive.org/web/20190814203701/https://www.ictshore.com/python/python-ping-tutorial/
'''

#!/usr/bin/python3

from datetime import datetime
import time
from pythonping import ping


def user_ping():
    user_input = input("Enter IPv4 address: ")
    return user_input


def test_ping(ip_address):
    start_time = datetime.now()
    filename=f'{start_time.strftime("%Y-%m-%d_%H:%M:%S")}_ping_log_{ip_address}.txt'
    with open(f'{filename}', 'a') as file:
        while True:
            response = ping(ip_address, count=1)
            now = datetime.now()
            status = f'{now.strftime("%Y-%m-%d_%H:%M:%S")} Network ACTIVE to {ip_address}' if response.success() else f'{now.strftime("%Y-%m-%d_%H:%M:%S")} Network INACTIVE to {ip_address}'
            print(status)
            file.write(f'{status}\n')
            time.sleep(2)

if __name__ == "__main__":
    ping_address = user_ping()
    test_ping(ping_address)
