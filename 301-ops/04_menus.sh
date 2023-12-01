#!/bin/bash

# Script Name:                  menus
# Author:                       Marcus Nogueira
# Date of latest revision:      11/30/2023
# Purpose:                      PURPOSE
# Resources Used:               https://unix.stackexchange.com/questions/487141/get-every-ip-except-for-the-loopback-device 


# Declaration of variables

# Declaration of functions
function menu(){

  while :
    do
      clear
      echo ""
      echo "  -------------------------------"
      echo "  |            Menu             |"
      echo "  -------------------------------"
      echo "  | 1. Hello                    |"
      echo "  | 2. Ping Self                |"
      echo "  | 3. IP Info                  |"
      echo "  | 4. Quit                     |"
      echo "  -------------------------------"
      read -p " Enter option: " menuChoice

      
      case $menuChoice in
        1) helloworld;;
        2) ping_self;;
        3) ip_info;;
        4) break;;
        *) echo "";echo "Invalid choice";echo "";;
      esac

      read -p " Press ENTER to return to menu."
    done
    quit_menu
   # read -p " Press ENTER to return to menu."
  }

function helloworld(){
  clear
  figlet "Hello World" -f "DOS Rebel" | lolcat --animate --speed 60
}

function ping_self() {
  clear
  figlet "Ping Self" -f "ANSI Shadow" | lolcat --animate --speed 60
  ping -c 5 localhost
  echo ""
  return
}

function ip_info(){
  clear
  figlet "ip info" -w 120 -f Fraktur | lolcat --animate --speed 70
  ip a show scope global
  echo ""
}

function quit_menu(){
  clear 
  figlet -c "See ya space cowboy" -f "Rowan Cap" | lolcat
}

# Main
menu

# End
