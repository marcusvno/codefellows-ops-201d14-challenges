""" 
    Author:                       Marcus Nogueira
    Date of latest revision:      12/08/2023
    Purpose:                      Learn about Python File Handling
"""

# Libary Imports
import os

# Variables

# Functions


def user_input():
    while True:
        dir_path = input("\nEnter a directory path: ")
        
        # This is the same as   if os.path.isdir(dir_path) == False
        if not os.path.isdir(dir_path):
            print("That directory path does not exist. Please try again.")
            continue

        file_name = input("Enter a file name (without extension): ") + ".txt"
        fullpath = os.path.join(dir_path, file_name)
        if os.path.exists(fullpath):
            print("This file already exists. Please enter a new filename.\n")
        else:
            return fullpath


def file_manip(full_path):
    with open(full_path, "w") as file:
        file.write("The story so far: \n")
        file.write("In the Beginning, the Universe was created.\n")
        file.write(
            "This has made a lot of people very angry and been widely regarded as a Bad Move.\n")

    with open(full_path, "r") as file:
        lines = file.readlines()
        print(f"\n{lines[0]}")

    os.remove(full_path)


# main block
if __name__ == "__main__":
    filepath = user_input()
    file_manip(filepath)
