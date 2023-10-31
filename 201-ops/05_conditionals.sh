#!/bin/bash

# Script Name:                  05_conditionals
# Author:                       Marcus Nogueira
# Date of latest revision:      10/30/1986
# Purpose:                      Determine if a file or directory exists
# Requirements:                 Must use one array/loop/conditional

# Declaration of variables

menuChoice=""

# Declaration of functions

function checker(){
  while:
    do
  
      echo ""
      echo "  -------------------------------"
      echo "  |      File/Dir Checker       |"
      echo "  -------------------------------"
      echo "  | 1. Check Directory Exists   |"
      echo "  | 2. Check File Exists        |"
      echo "  | 3. Quit                     |"
      echo "  -------------------------------"
      read -p " Enter option: " menuChoice

      
      case $menuChoice in
        1) read -p " Enter directory: " dirName
          if [ -d $dirName ]; then
            fullpath=realpath $dirName
            echo
            echo " Checking if $fullpath exists."
            echo " Directory exists."
            echo
          fi
          ;;
        3) break
      esac
                
    done

  }


# Main
checker
# End
