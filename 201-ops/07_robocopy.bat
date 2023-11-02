rem Disables the echoing of commands. Otherwise you would see things like "/set p sourcePath="
@echo off

rem When used in a batch file, setlocal enabledelayedexpansion makes changes to environment variables local to the current batch file and limits their scope.
setlocal enabledelayedexpansion

rem Prompts the user and stores the answer in the sourcePath variable.
set /p sourcePath=Enter the source folder path:

rem Prompts the user and stores the answer in the destinatioPath variable.
set /p destinationPath=Enter the destination folder path:

rem Checks if sourcePath is an existing folder.
if not exist "!sourcePath!\" (

    rem Reports that the source folder was not found. 
    echo Error: Source folder does not exist.

    rem Goes to End of File and skips of the rest of the code; effectively ends the bat from running further. Similar to break in a loop.
    goto :eof
)

rem Checkes if destinationpath is an existing folder.
if not exist "!destinationPath!\" (

    rem Reports that the destination folder was not found. 
    echo Error: Destination folder does not exist.

    rem Goes to End of File and skips of the rest of the code; effectively ends the bat from running further. Similar to break in a loop.
    goto :eof
)

rem Runs ropocopy copying the path provided in prompts above. Copies the source folder to the destination. Copies directories as well even if they're empty.
robocopy "!sourcePath!" "!destinationPath!" /E

rem Check robocopy for any errors of level 8 or higher which are failures.
if errorlevel 8 (

    rem If errors were found then informs the user.
    echo Error: ROBOCOPY encountered errors during the copy operation.

rem If no errors were found, complete the following...
) else (
    
    rem ...and prints a message saying the copy was succesfully made.
    echo Copy operation completed successfully.
)

rem Indicates the end of the code
:end

rem Ends localiztion of local set of envrionment variables.
endlocal
