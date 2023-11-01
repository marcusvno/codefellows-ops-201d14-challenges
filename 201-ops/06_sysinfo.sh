#!/bin/bash

# Script Name:                  06_sysinfo
# Author:                       Marcus Nogueira
# Date of latest revision:      10/31/2023
# Purpose:                      Display and filter system information from lshw with grep
# Citations:                    ChatGPT for learning the regex syntax for grep and the filter at the end of line 15 ram_info


# Declaration of functions

function sysinfo(){
  title=$(figlet "$(hostname)")
  cpu_info=$(lshw -class CPU 2>/dev/null | grep -E 'product:|vendor:|physical id:|bus info:|width:')
  ram_info=$(lshw -class memory 2>/dev/null | grep -A3 "description: System Memory" | grep -vE "^\*-memory|slot:")
  display_info=$(lshw -class display 2>/dev/null | grep -E 'description:|product:|physical id:|bus info:|width:|clock:|capabilities:|configuration:|resources:')
  network_info=$(lshw -class network 2>/dev/null | grep -E 'description:|product:|vender:|physical id:|bus info:|logical name:|version:|serial:|size:|capacity:|width:|clock:|capabilities:|resources:')
  bios_info=$(dmidecode | grep -A6 "BIOS Information")
  
  displaySysInfo
  
}


function displaySysInfo(){

echo "$title"
echo -e "   CPU:\n$cpu_info\n"
echo -e "   RAM:\n$ram_info\n"
echo -e "   DISPLAY ADAPTER:\n$display_info\n"
echo -e "   NETWORK ADAPTER:\n$network_info\n"
echo -e "   $bios_info\n"



}



# Main

sysinfo

# End
