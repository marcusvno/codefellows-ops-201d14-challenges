# Script Name:                  System Process Commands
# Author:                       Marcus Nogueira
# Date of latest revision:      11/03/2023
# Purpose:                      Analyze, initialize, and terminate processes using PowerShell

#Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.
function CPU_SORT { 
  Get-Process | Sort-Object CPU -Descending 
}

#Print to the terminal screen all active processes ordered by highest Process Identification Number at the top.
function ID_SORT {
  Get-Process | Sort-Object ID -Descending 
}

#Print to the terminal screen the top five active processes ordered by highest Working Set (WS(K)) at the top.
function TOP5_WS {
  Get-Process | Sort-Object WS -Descending | Select-Object -First 5
}

#Start a browser process (such as Google Chrome or MS Edge) and have it open https://owasp.org/www-project-top-ten/.
function CHROME_URL {
  Start-Process "chrome.exe" -ArgumentList "https://owasp.org/www-project-top-ten/"
}

#Start the process Notepad ten times using a for loop.
function OPEN_PROCESS{
    for ($i = 0; $i -lt $args[0]; i++) {
    Start-Process "notepad.exe"
  }
}

#Close all instances of the Notepad.
Stop-Process -Name notepad

#Kill a process by its Process Identification Number. Choose a process whose termination won’t destabilize the system, such as Google Chrome or MS Edge.
Stop-Process -Id 512

#Stretch Goals:
#Embed each task above into its own function.
#Create a menu which lets the user choose between each function.

function
