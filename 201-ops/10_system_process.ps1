# Script Name:                  System Process Commands
# Author:                       Marcus Nogueira
# Date of latest revision:      11/03/2023
# Purpose:                      Analyze, initialize, and terminate processes using PowerShell

#Print to the terminal screen all active processes ordered by highest CPU time consumption at the top.
function sort_cpu { 
  Get-Process | Sort-Object CPU -Descending 
}

#Print to the terminal screen all active processes ordered by highest Process Identification Number at the top.
function sort_id {
  Get-Process | Sort-Object ID -Descending 
}

#Print to the terminal screen the top five active processes ordered by highest Working Set (WS(K)) at the top.
function sort_ws {
  $how_many = Read-Host " How many processes to display (#): "
  Get-Process | Sort-Object WS -Descending | Select-Object -First $how_many
}

#Start a browser process (such as Google Chrome or MS Edge) and have it open https://owasp.org/www-project-top-ten/.
function open_chrome {
  $url = Read-Host " Enter URL"

  Start-Process "chrome.exe" -ArgumentList $url
}

#Start the process Notepad ten times using a for loop.
function launch_process {
  $target_app = Read-Host "Enter process [path]"
  $copies = Read-Host " Enter how many to open [#]"


  for ($i = 0; $i -lt $copies - 1; $i++) {
    Start-Process $target_app
  }
}

#Close all instances of the Notepad.
function kill_process {
  Get-Process | Sort-Object ProcessName
  $target_name = Read-Host " Enter process name"

  Stop-Process -Name $target_name
}

#Kill a process by its Process Identification Number. Choose a process whose termination won’t destabilize the system, such as Google Chrome or MS Edge.
function kill_pid {
  sort_id
  $target_pid = Read-Host " Enter process ID"
  Stop-Process -Id $target_pid
}

#Stretch Goals:
#Embed each task above into its own function.
#Create a menu which lets the user choose between each function.

function show_menu {

  $loop_quit = $true
  while ($loop_quit) {
    Clear-Host
    
    Write-Host "#################################################"
    Write-Host "##             PROCESS MANIPULATOR             ##"
    Write-Host "##                                             ##"
    Write-Host "##  1. Sort By CPU                             ##"
    Write-Host "##  2. Sort by ID                              ##"
    Write-Host "##  3. Sort by Working Set                     ##"
    Write-Host "##  4. Start a Process                         ##"
    Write-Host "##  5. Kill a Process by Name                  ##"
    Write-Host "##  6. Kill a Process by ID                    ##"
    Write-Host "##  7. Launch Chrome                           ##"
    Write-Host "##  8. Quit                                    ##"
    Write-Host "##                                             ##"
    Write-Host "#################################################"
    Write-Host "" #Line break

    $menu_choice = Read-Host " Enter option "

    switch ($menu_choice) {
      "1" { sort_cpu }
      "2" { sort_id }
      "3" { sort_ws }
      "4" { launch_process }
      "5" { kill_process }
      "6" { kill_pid }
      "7" { open_chrome }
      "8" { $loop_quit = $false }
    }

    Read-Host " Press Enter to continue"
    
  }
}


show_menu
