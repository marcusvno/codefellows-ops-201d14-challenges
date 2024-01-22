#    Author:                       Marcus Nogueira
#    Date of latest revision:      01/21/2024
#    Purpose:                      Use PowerShell to:
#     - Ensure 'Configure SMB v1 Client Driver' is set to 'Enabled: Disable Driver (recommended)
#     - Ensure 'Password must meet complexity requirements' is Set to "Enabled"
#   Resource: 


# Import necessary modules
Import-Module ActiveDirectory
Import-Module GroupPolicy

# Modify the Default Domain Password Policy for Password Complexity
try {
    Set-ADDefaultDomainPasswordPolicy -ComplexityEnabled $true
    Write-Host "Password complexity has been enabled."
} catch {
    Write-Host "An error occurred setting password complexity: $_"
}

# Ensure you are running as Administrator
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator"))
{
    Write-Host "You must run PowerShell as an Administrator to make these changes."
} else {
   try {
    Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol -NoRestart
    Write-Host "SMBv1 has been disabled."
} catch {
    Write-Host "An error occurred: $_"
}
}

# Refresh Group Policy
try {
    gpupdate /force
    Write-Host "Group Policy update has been forced."
} catch {
    Write-Host "An error occurred while forcing Group Policy update: $_"
}