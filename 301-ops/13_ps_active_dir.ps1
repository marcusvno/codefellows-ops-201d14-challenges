#    Author:                       Marcus Nogueira
#    Date of latest revision:      12/13/2023
#    Purpose:                      Learn about Python automation with Active Directory

Import-Module ActiveDirectory

# Function accepts a prompt, presents it to the user, checks if the input is empty or not. Returns empty or input. Useful for skipping questions. 
function Get-Input{
    param ([string]$prompt)
    Write-Host $prompt
    $input = Read-Host
    if (-not [string]::IsNullOrWhiteSpace($input)){
        return $input
    }
    return $null
}

#Check if OU exists, if not create it.
$OUName = "ExampleOU"
if (-not (Get-ADOrganizationUnit -Filter "Name -eq '$OUName'" -ErrorAction SilentlyContinue)){
    New-ADOrganizationalUnit -Name "ExampleOU" -Path "DC=corp,DC=globexpower,DC=com"
}

# Loops through the prompts, submits to the Active Directory, and then asks if the user would like to do it again for another account. 
do {
    $firstName = Get-Input -prompt "Enter First Name: "
    $lastName = Get-Input -prompt "Enter Last Name: "
    $title = Get-Input -prompt "Enter Title: "
    $department = Get-Input -prompt "Enter Department: "
    $company = Get-Input -prompt "Enter Company: "
    $location = Get-Input -prompt "Enter Location: "
    $email = Get-Input -prompt "Enter Email: "

    $OUPath = "OU=ExampleOU,DC=corp,DC=globexpower,DC=com" #In the future rewrite this as another prompt or for whatever domain the project calls for.

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
        -AccountPassword (ConvertTo-SecureString -AsPlainText "Solarwinds123" -Force) `
        -ChangePasswordAtLogon $true

    $addAnother = Get-Input -prompt "Add another user (y/n): "
} while ($addAnother -eq "y")

