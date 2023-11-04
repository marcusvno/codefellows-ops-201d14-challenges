#!/bin/bash

# Script Name:                  Functions
# Author:                       Marcus Nogueira
# Date of latest revision:      10/25/2023
# Purpose:                      Prints the login history of this system. Repeat 3x.

# Declaration of variables
# Declaration of functions
loginHistory(){
  last
  echo "This is the login history."
	echo #line break
}

searchHistory(){
	read -p "Filter for a User? (y/n) " filterResponse
	
	if [[ $filterResponse == "y" || $filterResponse == "Y" ]]; then
			read -p "Enter username: " searchUser
			echo "Filtering for $searchUser : "
			echo # line break
			last | grep "$searchUser"
		else 
			echo "Filter canceled."
	fi

}


# Main

for i in {1,2,3}; do
	loginHistory
done

searchHistory
# End

# Citations
# For user input: https://ryanstutorials.net/bash-scripting-tutorial/bash-input.php
