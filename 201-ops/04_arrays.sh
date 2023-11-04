#!/bin/bash

# Script Name:                  2_arrays.sh
# Author:                       Marcus Nogueira
# Date of latest revision:      10/26/2023
# Purpose:                      Creates 4 directories, puts the names in an array, references array to create a new text file in each directory

# Declaration of variables
declare -a dirArray
# Declaration of functions
multiDir(){
  read -p "Enter number of directories to create: " numDir
  
  for ((i=1; i<=$numDir; i++));
  do
    mkdir dir$i
    dirArray+=(dir$i)
    echo "Creating..." ${dirArray[i-1]}
  done

  read -p "Would you like to add a README.md to the folders (y/n): " readmeAnswer

	if [[ $readmeAnswer == "y" || $readmeAnswer == "Y" ]]; then
		for ((i=0; i<=(numDir-1); i++));
    do
    	touch ${dirArray[i]}/README.md
      echo "Adding README.md to" ${dirArray[i]}
    done
	else 
		echo "README.me not added."
	fi
}

# Main
multiDir
# End

# Citations : 
# For the syntax in declaring an empty array https://stackoverflow.com/questions/18921350/shell-script-correct-way-to-declare-an-empty-array
# Idea of using a for loop in the style of C : Mike Sineiro
# Syntax for C-style for loop: https://www.geeksforgeeks.org/bash-scripting-for-loop/
