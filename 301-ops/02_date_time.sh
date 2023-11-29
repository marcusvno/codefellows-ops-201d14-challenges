#!/bin/bash

# Script Name:                  Appends Date and Time to File Name
# Author:                       Marcus Nogueira
# Date of latest revision:      11/27/2023
# Purpose:                      Copies /var/log/syslog to current working directory and adds date/time to the filename.

# Declaration of variables

date_time=$(date +%Y-%m-%dT%H:%M:%S%Z)

# Declaration of functions
logs_copy(){
  cp /var/log/syslog syslog_$date_time
  echo "File created -- syslog_$date_time"
}


# Main
echo "Getting current Date and Time.."
sleep 0.5
echo "Current Time: $date_time"
sleep 0.5
echo "Copying syslog to current working directory."
sleep 0.5
logs_copy

# End
