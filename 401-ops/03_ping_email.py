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
https://archive.is/Tl9bj#selection-1833.0-1859.44


REQUIRED PACKAGES TO INSTALL:
pythonping
python-dotenv

'''

#!/usr/bin/python3

import os #Used with dotenv
from datetime import datetime #For timestamps
import time #To space out our pings
from dotenv import load_dotenv #Loads in our environment variables
from pythonping import ping #Used to ping our targets
import smtplib 
import ssl 
from email.message import EmailMessage

load_dotenv() #Load in environment variables

def user_ping():
    user_input = input("Enter IPv4 address: ")
    return user_input

def receiver():
    user_input = input("Enter target email for notifications: ")
    return user_input

def send_email(receiver_email, subject, body):
    message = EmailMessage()
    message["From"] = os.getenv('EMAIL_ADDRESS')

def test_ping(ip_address, notification_email):
    """Pythonping requires elevated permissions or it will error out. Run with sudo."""
    
    start_time = datetime.now()
    filename = f'{start_time.strftime("%Y-%m-%d_%H:%M:%S")}_ping_log_{ip_address}.txt'
    
    with open(f'{filename}', 'a') as file:
        while True:
            response = ping(ip_address, count=1)
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H:%M:%S")
            # status = f'{now.strftime("%Y-%m-%d_%H:%M:%S")} Network ACTIVE to {ip_address}' if response.success(
            status = "ACTIVE" if response.success() else "INACTIVE" #Cleaner version than above
            print(f'{timestamp} - Network {status} - {ip_address}')
            file.write(f'{timestamp} - Network {status} - {ip_address}\n')
            time.sleep(2)


if __name__ == "__main__":
       
    ping_address = user_ping()
    notification_addr = receiver()
    test_ping(ping_address, notification_addr)
