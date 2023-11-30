#!/bin/bash

# Script Name:                  03_file_permissions.sh
# Author:                       Marcus Nogueira
# Date of latest revision:      11/29/2023
# Purpose:                      Change the file permissions of all the files within a directory.

# Declaration of variables
read -p "Enter the directory path: " directory
read -p "Enter the permissions number: " perms

# Declaration of functions
change_perms(){
  cd "$directory" && chmod $perms *
  ls -l $directory
}

# Main
change_perms

# End
