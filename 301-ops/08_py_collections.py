# Author:                       Marcus Nogueira
# Date of latest revision:      12/06/2023
# Purpose:                      Work with Lists in Python

# Libraries imported
import os
import time

# Declaration of variables
# ANSI color codes for text colors
BLACK = "\033[30m"      # Black text
RED = "\033[31m"        # Red text
GREEN = "\033[32m"      # Green text
YELLOW = "\033[33m"     # Yellow text
BLUE = "\033[34m"       # Blue text
MAGENTA = "\033[35m"    # Magenta text
CYAN = "\033[36m"       # Cyan text
WHITE = "\033[37m"      # White text
BG_RED = "\033[41m"     # Red Background

RESET = "\033[0m"       # Reset all formatting
BOLD = "\033[1m"        # Bold text
BLINK = "\033[5m"       # Blinking text
DIM = "\033[2m"         # Dim text



ANSI_COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[37m",  # White
]

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter",
           "Saturn", "Uranus", "Neptune", "Pluto", "Eris"]

os.system('clear')
time.sleep(0.5)
os.system('figlet Planets -w 300 -f "cosmic" | lolcat')
time.sleep(1)

print(
    f'\nThe {DIM}{RED}fourth{RESET} planet of the solar system is {RED}{planets[3]}{RESET}.\n')
time.sleep(0.5)
print(f'The {DIM}{GREEN}sixth{RESET} through {WHITE}{DIM}tenth{RESET} planet of the {YELLOW}Sol system{RESET} are:\n')
time.sleep(0.5)
for i, planet in enumerate(planets[5:10]):
    color = ANSI_COLORS[i % len(ANSI_COLORS)]
    print(f' {i+int(6)}) {color}{planet}{RESET}')
    time.sleep(0.6)

print(f'\n{BLINK}WARNING  WARNING  WARNING  WARNING  WARNING  WARNING  WARNING  WARNING {RESET}')
time.sleep(2.5)
print(f'{GREEN}\nAliens{RESET} have replaced {CYAN}{planets[6]}{RESET}!')
time.sleep(0.5)
planets[6] = "Onion"
print(f'It is now an enormous {YELLOW}{planets[6]}{RESET}!')


