## RODAR

$DesktopPath = [Environment]::GetFolderPath("Desktop")
Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/Lucas-HGB/Dotfiles/main/Pai.py" -OutFile "$DesktopPath\MonitorarImagem.py"
Invoke-WebRequest "https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe" -OutFile "$DesktopPath\Python3.exe"
Write-Host "Após instalar o python com as definições padrões, aperte ENTER nessa tela do Powershell"
Read Nothing

& "$DesktopPath\Python3.exe"

$AppData = $env:LOCALAPPDATA
& "$AppData\Programs\Python\Python39\python.exe -m pip install pillow"

Write-Host "Para rodar o programa, clique 2x no arquivo 'MonitorarImagem.py', localizado em seu Desktop (:"
read Nothing
