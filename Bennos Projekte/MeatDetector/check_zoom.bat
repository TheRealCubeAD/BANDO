tasklist /fi "ImageName eq CptHost.exe" /fo csv 2>NUL | find /I "cpthost.exe">NUL
if "%ERRORLEVEL%"=="0" exit /b 2
exit /b 0