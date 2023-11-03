#This script is written for PowerShell 7.3, and NOT Windows PowerShell 5.1, as PowerShell 7 is the crossplatform industry standard version of PowerShell while PowerShell 5.1 is Windows only.


#Output all events from the System event log that occurred in the last 24 hours to a file on your desktop named last_24.txt in a hastable format, seperated by providers and in descending order (newest to oldest)
Get-WinEvent -FilterHashtable @{ LogName='System'; StartTime=(Get-Date).AddDays(-1) } | Sort-Object TimeCreated -Descending | Format-Table -Wrap -AutoSize | Out-File "C:\users\marcus\Desktop\last_24.txt"


#Output all “error” type events from the System event log to a file on your desktop named errors.txt in a hastable format, seperated by providers and in descending order (newest to oldest)
Get-WinEvent -FilterHashtable @{ LogName='System'; Level=2 } | Sort-Object TimeCreated -Descending |  Format-Table -Wrap -AutoSize | Out-File "C:\users\marcus\Desktop\errors.txt"

#Print to the screen all events with ID of 16 from the System event log in a hastable format, seperated by providers and in ascending order (oldest to newest)
Get-WinEvent -FilterHashtable @{ LogName='System'; Id='16'} | Sort-Object TimeCreated | Format-Table -Wrap -Autosize

#Print to the screen the most recent 20 entries from the System event log (oldest to newest)
Get-WinEvent -LogName 'System' -MaxEvents 20 | Sort-Object TimeCreated | Format-Table -Wrap -AutoSize


#Print to the screen all sources of the 500 most recent entries in the System event log (oldest to newest)
Get-WinEvent -LogName 'System' -MaxEvents 500 | Sort-Object TimeCreated | Format-Table -Wrap -AutoSize
