# Author:                       Marcus Nogueira
# Date of latest revision:      12/04/1986
# Purpose:                      A Python script that executes a few bash commands successfully.

# Imports
import os
import subprocess
import time

# Declaration of variables
BLUE = "\033[34m"  # Blue text
RESET = "\033[0m"  # Reset to default color


# Declaration of functions
def snake_bash():
    os.system("clear")
    os.system('figlet "Punching Snakes" -f "3d" | lolcat')
    print("\n\n")
    time.sleep(1)

    print(f'{BLUE}LOGGED IN USER: {RESET}')
    os.system('whoami')
    print("")
    time.sleep(1)
    ip_output = subprocess.getoutput(
        "ip a show eno1 | grep -oP 'inet \K\d{1,3}(\.\d{1,3}){3}'")
    print(f'{BLUE}CURRENT IP ADDRESS:\n{RESET}{ip_output}')
    print("")
    time.sleep(1)

    print(f'{BLUE}THIS PC\'S HARDWARE:{RESET}')
    os.system('sudo lshw -short')


# Main
if __name__ == "__main__":
    snake_bash()

# End
