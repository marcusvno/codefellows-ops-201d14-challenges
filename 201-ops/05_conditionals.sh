#!/bin/bash

# Script Name:                  05_conditionals
# Author:                       Marcus Nogueira
# Date of latest revision:      10/30/1986
# Purpose:                      Determine if a file or directory exists
# Requirements:                 Must use one array/loop/conditional

# Declaration of variables

menuChoice=""

# Declaration of functions
#function menu(){

#}


function checker(){

  while :
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
        1) dirCheck;;
        2) fileCheck;;
        3) break;;
        *) echo " Invalid choice";;
      esac

      read -p " Press ENTER to return to menu."
    done

  }

function dirCheck(){

  read -p " Enter directory: " dirName
  local fullpath

 # Check if the first character is '~' and expand it (Citation: ChatGPT used to figure out this expansion of ~)
  if [[ ${dirName:0:1} == "~" ]]; then
    dirName="${HOME}${dirName:1}"
  fi


  if [ -d "$dirName" ]; then
    fullpath=$(realpath "$dirName")
    echo
    echo " Checking $fullpath "
    echo " Directory exists."
    echo
  else
    echo " Directory does NOT exist."
  fi
}

function fileCheck(){
  
  local dirFileArray
  
  read -p " Is the file in the current directory: (y/n) " currentDir

  if [[ $currentDir == 'y' || $currentDir == 'Y' ]]; then
    read -p " Enter filename1: " pwdFile
    fullpath=$(realpath "$pwdFile")
    
    echo
    echo " Checking $fullpath "
    
    if [ -f "$fullpath" ]; then  
      echo " ...File exists."  
    else
      echo " ...File does NOT exist."
    fi

  elif [[ $currentDir == 'n' || $currentDir == 'N' ]]; then
    read -p " Enter directory (use absolute path): " pathDir
    dirFileArray+=("$pathDir")
    read -p " Enter filename2: " pathFile
    dirFileArray+=("$pathFile")
    echo " Checking ${dirFileArray[0]}/${dirFileArray[1]}"

    if [ -f "${dirFileArray[0]}/${dirFileArray[1]}" ]; then
      echo " ...File exists."
    else
      echo " ...File does NOT exist."
    fi
  else
    echo " Not a valid option."
  fi  
  echo       
}



# Main
checker
# End
