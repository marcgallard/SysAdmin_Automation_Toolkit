@ECHO OFF

REM Get current folder path where .bat is running and remove trailing backslash
set "CURRENT_DIR=%~dp0"
set "CURRENT_DIR=%CURRENT_DIR:~0,-1%"

REM Define Powershell command to run
set "BLOCK_PS_CMD=powershell.exe -NoProfile -ExecutionPolicy Bypass -Command \"Start-Process -FilePath '%CURRENT_DIR%\BlockExe.bat' -ArgumentList '%%1' -Verb RunAs\""
set "ALLOW_PS_CMD=powershell.exe -NoProfile -ExecutionPolicy Bypass -Command \"Start-Process -FilePath '%CURRENT_DIR%\AllowExe.bat' -ArgumentList '%%1' -Verb RunAs\""

REM Define the registry path, its keys, and subkeys for Block Exe
set "REG_PATH=HKEY_CLASSES_ROOT\*\shell\BlockExe"
reg add "%REG_PATH%" /ve /d "Block Exe Firewall" /f
reg add "%REG_PATH%" /v "Icon" /t REG_SZ /d "imageres.dll,-105" /f
reg add "%REG_PATH%" /v "Position" /t REG_SZ /d "Bottom" /f
reg add "%REG_PATH%\command" /ve /d "%BLOCK_PS_CMD%" /f

REM Define the registry path, its keys, and subkeys for Allow Exe
set "REG_PATH=HKEY_CLASSES_ROOT\*\shell\AllowExe"
reg add "%REG_PATH%" /ve /d "Allow Exe Firewall" /f
reg add "%REG_PATH%" /v "Icon" /t REG_SZ /d "imageres.dll,-106" /f
reg add "%REG_PATH%" /v "Position" /t REG_SZ /d "Bottom" /f
reg add "%REG_PATH%\command" /ve /d "%ALLOW_PS_CMD%" /f

echo Registry updated successfully

:END
PAUSE