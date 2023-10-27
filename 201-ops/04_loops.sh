#!/bin/bash

# Script Name:                  04_loops.sh
# Author:                       Marcus Nogueira
# Date of latest revision:      10/27/2023
# Purpose:                      Displays running processes, asks the user for a PID, then kills the process with that PID. Starts over at steo 1 until user exits with CTRL+C

# Declaration of variables

# Declaration of functions
kill_process(){
  
  while :
  do
    ps aux
    echo #line break
    read -p "Enter PID: " process_id
    if kill -9 $process_id 2>/dev/null; then
      echo "Successfully killed process with PID $process_id."
    else
      echo "Failed to kill process with PID $process_id. It may not exist or you may lack necessary permissions."
    fi
    read -p "Kill another process? (y/n): " continue_killing
    if [[ $continue_killing == "n" || $continue_killing == "N" ]]; then
      break
    fi

  done
}

# Main
kill_process
# End

# Citation: ChatGPT helped with explaining the usage of "2>/dev/null" for successful command execution in shell scripting. 
# Citation: Used https://www.cyberciti.biz/faq/bash-while-loop/ to simplify writing the infinite loop
