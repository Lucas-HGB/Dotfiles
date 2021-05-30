$params = @{
  Name = "KeyboardShortcuts"
  BinaryPathName = 'S:\Documents\Programs\KeyboardShortcuts.exe'
  DisplayName = "Keyboard shortcuts"
  StartupType = "Automatic"
  Description = "Script Python que controla diversos shortcuts; autocompletes; e funções do teclado"
}

New-Service @params
