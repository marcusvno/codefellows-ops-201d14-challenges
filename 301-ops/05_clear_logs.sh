#!/bin/bash

# Script Name:                  Clear Logs
# Author:                       Marcus Nogueira
# Date of latest revision:      12/01/2023
# Purpose:                      Compress,backup, and clear logs.

# Declaration of variables
BACKUP_DIR="/var/log/backups/"
LOG_TARGET1="/var/log/syslog"
LOG_TARGET2="/var/log/wtmp"
BACKUP_LOCATION_FILE1=""
BACKUP_LOCATION_FILE2=""

BACKUP_FILENAME1=""
BACKUP_FILENAME2=""

FILE_NAME1=$(basename "$LOG_TARGET1")
FILE_NAME2=$(basename "$LOG_TARGET2")



# Test variables for ensuring the script works as intended without having to deal with messing up the system logs.
 #BACKUP_DIR="/home/marcus/Documents/temp/backups"
 #LOG_TARGET1="/home/marcus/Documents/temp/syslog"
 #LOG_TARGET2="/home/marcus/Documents/temp/wtmp"
 #FILE_NAME1=$(basename "$LOG_TARGET1")
 #FILE_NAME2=$(basename "$LOG_TARGET2")

# ANSI color codes
GREEN="\033[0;32m"
PINK="\033[0;35m"
NO_COLOR="\033[0m" # No color (reset to default)

# Declaration of functions

function dir_check(){

  #Declare the directory check
  echo -e "Checking for ${GREEN}${BACKUP_DIR}${NO_COLOR}" 
  echo ""
  sleep 0.5


  #Test for backup directory & creates if missing. Informs user if it exists.
  if [ ! -d $BACKUP_DIR ]; then
    echo -e "${GREEN}${BACKUP_DIR}${NO_COLOR} not found."
    sleep 1
    echo -e "Creating ${GREEN}${BACKUP_DIR}${NO_COLOR}"
    sudo mkdir -p $BACKUP_DIR
    sleep 0.5
    echo -e "${GREEN}${BACKUP_DIR}${NO_COLOR} created."
    echo""

  else
    echo -e "${GREEN}${BACKUP_DIR}${NO_COLOR} found."
    echo ""
    sleep 1
  fi

}

function backup_logs(){
  
  timed_log1="$LOG_TARGET1-$(date +%Y%m%dH%HM%MS%S)"
  TO_BACK_UP1="$timed_log1.7z"
  BACKUP_FILENAME1=$(basename $TO_BACK_UP1)
  BACKUP_LOCATION_FILE1="$BACKUP_DIR/$BACKUP_FILENAME1"


  echo -e "Compressing ${GREEN}${LOG_TARGET1}${NO_COLOR}"
  sleep 0.5
  sudo 7z a $timed_log1.7z $LOG_TARGET1 > /dev/null
 
  echo -e "Compression of ${GREEN}${FILE_NAME1}${NO_COLOR} complete!"
  echo ""
  sleep 1

  echo -e "Moving of ${GREEN}${BACKUP_FILENAME1}${NO_COLOR} to ${PINK}${BACKUP_DIR}${NO_COLOR}"
  sudo mv ${timed_log1}.7z $BACKUP_DIR
  sleep 0.5
  echo -e "Completed relocation of ${GREEN}${BACKUP_FILENAME1}${NO_COLOR} to ${PINK}${BACKUP_DIR}${NO_COLOR}"
  sleep 1
  echo "" 

  timed_log2="$LOG_TARGET2-$(date +%Y%m%dH%HM%MS%S)"
  TO_BACK_UP2="$timed_log2.7z"
  BACKUP_FILENAME2=$(basename $TO_BACK_UP2)
  BACKUP_LOCATION_FILE2="$BACKUP_DIR/$BACKUP_FILENAME2"

  echo -e "Compressing ${GREEN}${LOG_TARGET2}${NO_COLOR}"
  
  sudo 7z a $timed_log2.7z $LOG_TARGET2 > /dev/null
  echo -e "Compression of ${GREEN}${FILE_NAME2}${NO_COLOR} complete!"
  echo ""
  sleep 1

  echo -e "Moving of ${GREEN}${BACKUP_FILENAME2}${NO_COLOR} to ${PINK}${BACKUP_DIR}${NO_COLOR}"
  sudo mv $TO_BACK_UP2 $BACKUP_DIR
  sleep 0.5
  echo -e "Completed relocation of ${GREEN}${BACKUP_FILENAME2}${NO_COLOR} to ${PINK}${BACKUP_DIR}${NO_COLOR}"
  echo ""

  sleep 1
  
}


function clear_logs() {

  echo -e "${GREEN}${FILE_NAME1}${NO_COLOR}    File Size: $(du -sh "$LOG_TARGET1" | awk '{print $1}')"

  echo -e "Clearing: ${GREEN}${LOG_TARGET1}${NO_COLOR}"
  sudo truncate -s 0 $LOG_TARGET1

  sleep 0.5
  echo "Cleared!"

  echo -e "${GREEN}${FILE_NAME1}${NO_COLOR}    File Size: $(du -sh "$LOG_TARGET1" | awk '{print $1}')"
  echo -e "${GREEN}${BACKUP_FILENAME1}${NO_COLOR}    File Size: $(du -sh "$BACKUP_LOCATION_FILE1" | awk '{print $1}')"
  echo ""
  sleep 0.5

  echo -e "${GREEN}${FILE_NAME2}${NO_COLOR}    File Size: $(du -sh "$LOG_TARGET2" | awk '{print $1}')"
  echo -e "Clearing: ${GREEN}${LOG_TARGET2}${NO_COLOR}"
  sudo truncate -s 0 $LOG_TARGET2

  sleep 0.5
  echo "Cleared!"

  echo -e "${GREEN}${FILE_NAME2}${NO_COLOR}    File Size: $(du -sh $LOG_TARGET2 | awk '{print $1}')"
  echo -e "${GREEN}${BACKUP_FILENAME2}${NO_COLOR}    File Size: $(du -sh "$BACKUP_LOCATION_FILE2" | awk '{print $1}')"

}

function banner(){
  figlet "Log Killer" -f "ANSI Shadow" | lolcat --animate --speed 60
  echo ""
}


# Main

clear
banner
dir_check
backup_logs
clear_logs


# End
