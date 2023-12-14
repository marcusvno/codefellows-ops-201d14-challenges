#    Author:                       Marcus Nogueira
#    Date of latest revision:      12/13/2023
#    Purpose:                      Learn about Python automation with Active Directory

Import-Module ActiveDirectory

# Function accepts a prompt, presents it to the user, checks if the input is empty or not. Returns empty or input. Useful for skipping questions. 
function Get-Input {
    param ([string]$prompt)
    Write-Host $prompt
    $user_input = Read-Host
    if (-not [string]::IsNullOrWhiteSpace($user_input)) {
        return $user_input
    }
    return $null
}

do {
    $firstName = Get-Input -prompt "Enter First Name"
    $lastName = Get-Input -prompt "Enter Last Name"
    $title = Get-Input -prompt "Enter Title"
    $department = Get-Input -prompt "Enter Department"
    $company = Get-Input -prompt "Enter Company"
    $location = Get-Input -prompt "Enter Location"
    $email = Get-Input -prompt "Enter Email"

    # Check for the OU based on the Department
    $OUPath = "OU=$department,DC=corp,DC=globexpower,DC=com"
    if (-not (Get-ADOrganizationalUnit -Filter "Name -eq '$department'" -ErrorAction SilentlyContinue)) {
        New-ADOrganizationalUnit -Name $department -Path "DC=corp,DC=globexpower,DC=com"
    }

    # User creation
    New-ADUser -Name "$firstName $lastName" `
        -GivenName $firstName `
        -Surname $lastName `
        -SamAccountName ($firstName[0] + $lastName).ToLower() `
        -UserPrincipalName "$email" `
        -Path $OUPath `
        -Title $title `
        -Department $department `
        -Company $company `
        -Office $location `
        -EmailAddress $email `
        -Enabled $true `
        -AccountPassword (ConvertTo-SecureString "Solarwinds123" -AsPlainText -Force) `
        -ChangePasswordAtLogon $true

    $addAnother = Get-Input -prompt "Would you like to add another user? (Y/N)"
} while ($addAnother -eq "Y")
