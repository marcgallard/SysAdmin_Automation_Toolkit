@ECHO OFF

REM Parsing args
SET "exePath=%*"
SET "folderPath=%~dp1%"

REM Switching directories and getting folder name
CD /D "%folderPath%"
FOR %%i IN (.) DO SET baseFolderName=%%~nxi

REM Firewall changes

REM Add inbound rule
netsh advfirewall firewall add rule name="%baseFolderName%" dir=in action=block program="%exePath%" enable=yes profile=any >nul

REM Add outbound rule
netsh advfirewall firewall add rule name="%baseFolderName%" dir=out action=block program="%exePath%" enable=yes profile=any >nul

:END
PAUSE