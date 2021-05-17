$AppData = $env:LOCALAPPDATA
& "$AppData\Programs\Python\Python39\python.exe -m pip install pillow"

$Nothing = Read-Host -Prompt "Para rodar o programa, clique 2x no arquivo 'MonitorarImagem.py', localizado em seu Desktop (:"
