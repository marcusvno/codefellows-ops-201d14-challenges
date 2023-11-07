# Script Name:                  Automated Endpoint Configuration
# Author:                       Marcus Nogueira
# Date of latest revision:      11/06/2023
# Purpose:                      Automate Windows Endpoint

# Declaration of variables

# Declaration of functions


# Main

#Enable File and Printer Sharing
Set-NetFirewallRule -DisplayGroup "File And Printer Sharing" -Enabled True

#Allow ICMP traffic
netsh advfirewall firewall add rule name="Allow incoming ping requests IPv4" dir=in action=allow protocol=icmpv4 

#Enable Remote management
#Enable RDP connections
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

#Enable Network Level Authentication, an added layer of security for RDP
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name "UserAuthentication" -Value 1

#Remove Bloatware
iex ((New-Object System.Net.WebClient).DownloadString('https://git.io/debloat'))

#Enable HyperV
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All

#Disable SMBv1
Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force

# End
