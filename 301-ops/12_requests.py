""" 
    Author:                       Marcus Nogueira
    Date of latest revision:      12/12/2023
    Purpose:                      Learn about Python Request Library
"""

# Import Libraries
import requests as req
import os
import time

# Declaration of variables
BLUE = "\033[34m"  # Blue text
GREEN = "\033[32m"  # Green text
YELLOW = "\033[33m"  # Yellow text
RESET = "\033[0m"  # Reset to default color

# Declare Functions


def user_input():
    while True:
        print("  -----------------")
        print("  | 1. Get        |")
        print("  | 2. Post       |")
        print("  | 3. Put        |")
        print("  | 4. Delete     |")
        print("  | 5. Head       |")
        print("  | 6. Patch      |")
        print("  | 7. Options    |")
        print("  -----------------")
        choice = input("  Select one of the above: ")

        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            return choice
        else:
            print("Invalid choice. Please choose a valid number.")
            time.sleep(1.5)


def confirmation(url, method):
    while True:
        confirm = input(
            f'Confirm {GREEN}{method}{RESET} request to {YELLOW}{url}{RESET} (Y/N): ')
        if confirm.lower() in ["y", "n"]:
            break
        else:
            print("Invalid input. Please enter Y (for yes) or N (for no).")

    if confirm.lower() == 'y':
        match method:
            case "GET":
                response = req.get(url, timeout=30)
                return response
            case "POST":
                response = req.post(url, timeout=30)
                return response
            case "PUT":
                response = req.put(url, timeout=30)
                return response
            case "DELETE":
                response = req.delete(url, timeout=30)
                return response
            case "HEAD":
                response = req.head(url, timeout=30)
                return response
            case "PATCH":
                response = req.patch(url, timeout=30)
                return response
            case "OPTIONS":
                response = req.options(url, timeout=30)
                return response
    else:
        print("Canceling operation.")
        return "cancel"


def print_status(response_code):
    
    print("")
    
    if response_code.status_code == 200:
        print("Response code:", response_code.status_code,
              "OK - The request was successful.")
    elif response_code.status_code == 201:
        print("Response code:", response_code.status_code,
              "Created - The request was successful, and a new resource was created.")
    elif response_code.status_code == 204:
        print("Response code:", response_code.status_code,
              "No Content - The request was successful, but there is no additional information to send back.")
    elif response_code.status_code == 400:
        print("Response code:", response_code.status_code,
              "Bad Request - The request could not be understood or was missing required parameters.")
    elif response_code.status_code == 401:
        print("Response code:", response_code.status_code,
              "Unauthorized - Authentication failed or user does not have permissions.")
    elif response_code.status_code == 403:
        print("Response code:", response_code.status_code,
              "Forbidden - The server refuses to authorize the request.")
    elif response_code.status_code == 404:
        print("Response code:", response_code.status_code,
              "Not Found - The requested resource could not be found.")
    elif response_code.status_code == 405:
        print("Response code:", response_code.status_code,
              "Method Not Allowed - The specified method is not allowed for the resource.")
    elif response_code.status_code == 500:
        print("Response code:", response_code.status_code,
              "Internal Server Error - An unexpected condition was encountered on the server.")
    elif response_code.status_code == 502:
        print("Response code:", response_code.status_code,
              "Bad Gateway - The server received an invalid response from the upstream server.")
    elif response_code.status_code == 503:
        print("Response code:", response_code.status_code,
              "Service Unavailable - The server is not ready to handle the request.")
    elif response_code.status_code == 504:
        print("Response code:", response_code.status_code,
              "Gateway Timeout - The server did not receive a timely response from the upstream server.")
    elif response_code.status_code == 301:
        print("Response code:", response_code.status_code,
              "Moved Permanently - The requested resource has been permanently moved.")
    elif response_code.status_code == 302 or response_code.status_code == 303:
        print("Response code:", response_code.status_code,
              "Found/See Other - The requested resource resides temporarily under a different URL.")
    elif response_code.status_code == 304:
        print("Response code:", response_code.status_code,
              "Not Modified - The resource has not been modified since the specified version.")
    else:
        print("Your response code is", response_code.status_code,
              "which is not defined in this Python script.")
        exit()

    print("")
    for key, value in response_code.headers.items():
        print(f" -{key}: {value}")

    # print(response_code.headers)


# Main Block
if __name__ == "__main__":
    url = "https://" + str(input("Enter URL (no http): "))
    user_choice = user_input()
    match user_choice:
        case "1": status = confirmation(url, "GET")
        case "2": status = confirmation(url, "POST")
        case "3": status = confirmation(url, "PUT")
        case "4": status = confirmation(url, "DELETE")
        case "5": status = confirmation(url, "HEAD")
        case "6": status = confirmation(url, "PATCH")
        case "7": status = confirmation(url, "OPTIONS")

    if not status == "cancel":
        print_status(status)
