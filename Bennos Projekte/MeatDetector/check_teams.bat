tasklist /fi "ImageName eq msteams.exe" /fi "windowtitle eq Besprechung*" /fo csv 2>NUL | find /I "teams.exe">NUL
if "%ERRORLEVEL%"=="0" exit /b 2
exit /b 0