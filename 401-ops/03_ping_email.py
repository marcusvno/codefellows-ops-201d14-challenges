'''
Updated version of the ping sensor which uses an email daemon to send notifications. 

REQUIREMENTS:
    - Ask the user for an email address and password to use for sending notifications.
    - Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
    - Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

RESOURCES: 
https://github.com/alessandromaggio/pythonping
https://web.archive.org/web/20190814203701/https://www.ictshore.com/python/python-ping-tutorial/
https://www.tutorialspoint.com/How-to-print-current-date-and-time-using-Python
https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151
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
