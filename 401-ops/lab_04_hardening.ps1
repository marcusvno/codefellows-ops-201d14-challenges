#    Author:                       Marcus Nogueira
#    Date of latest revision:      01/21/2024
#    Purpose:                      Use PowerShell to:
#     - Ensure 'Configure SMB v1 Client Driver' is set to 'Enabled: Disable Driver (recommended)
#     - Ensure 'Password must meet complexity requirements' is Set to "Enabled"
#   Resource: 


Import-Module GroupPolicy # Import the module to edit group policies

# Modify the Default Domain Policy for Password Complexity
$defaultDomainPolicy = "Default Domain Policy"
Set-GPRegistryValue -Name $defaultDomainPolicy -Key "HKLM\Software\Microsoft\Windows NT\CurrentVersion\SecEdit\GptTmpl.inf" -ValueName "PasswordComplexity" -Value 1
# Set the SMB v1 client driver to disable
Set-GPRegistryValue -Name $defaultDomainPolicy -Key "HKLM\SYSTEM\CurrentControlSet\Services\mrxsmb10" -ValueName "Start" -Type DWORD -Value 4

# Refresh Group Policy
gpupdate /force

Write-Host "GPOs have been updated. Password complexity is enabled and SMB v1 client driver is disabled."
