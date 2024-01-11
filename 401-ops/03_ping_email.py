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
WARNING: THEY MUST BE INSTALLED WITH SUDO DUE TO pythonping REQUIRING ELEVATED PRIVILEGES WHEN YOU RUN THE SCRIPT (sudo pip install <package>)
pythonping
python-dotenv

'''

#!/usr/bin/python3

import os  # Used with dotenv
from datetime import datetime  # For timestamps
import time  # To space out our pings
from dotenv import load_dotenv  # Loads in our environment variables
from pythonping import ping  # Used to ping our targets
import smtplib
import ssl
from email.message import EmailMessage

load_dotenv()  # Load in environment variables


def user_ping():
    """User inputs target IPv4 address"""
    user_input = input("Enter IPv4 address: ")
    return user_input


def receiver():
    """User inputs email to receive ping status changes."""
    user_input = input("Enter target email for notifications: ")
    return user_input


def send_email(receiver_email, subject, body):
    """Sends email when status changes"""
    message = EmailMessage()
    message["From"] = os.getenv('EMAIL_ADDRESS')
    message["To"] = receiver_email
    message["Subject"] = subject
    message.set_content(body)

    # Add SSL
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(os.getenv('EMAIL_ADDRESS'), os.getenv('EMAIL_PWD'))
        smtp.send_message(message)


def test_ping(ip_address, notification_email):
    """Pythonping requires elevated permissions or it will error out. Run with sudo."""

    start_time = datetime.now()
    filename = f'{start_time.strftime("%Y-%m-%d_%H:%M:%S")}_ping_log_{ip_address}.txt'
    last_status = None

    with open(f'{filename}', 'a') as file:
        while True:
            response = ping(ip_address, count=1)
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d_%H:%M:%S")
            status = "ACTIVE" if response.success() else "INACTIVE"
            print(f'{timestamp} - Target: {ip_address} - Network {status}')
            file.write(
                f'{timestamp} - Target: {ip_address}\n - Network {status}')

            if last_status is not None and status != last_status:
                subject = "Ping Status Changed"
                body = f'{timestamp} - Target: {ip_address} - Network has changed from {last_status} to {status} '
                send_email(notification_email, subject, body)

            last_status = status
            time.sleep(2)


if __name__ == "__main__":
    ping_address = user_ping()
    notification_addr = receiver()
    test_ping(ping_address, notification_addr)
