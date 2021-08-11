$Folders = @("S:\Documents\Default.rdp", "S:\Pictures\Camera Roll", "S:\Pictures\Saved Pictures", "S:\Videos\AnyDesk"
"S:\Videos\Captures", "C:\Users\lucas\AppData\Local\Microsoft\Edge", "C:\hiberfil.sys", 
"C:\Users\lucas\AppData\Local\Mozilla\Firefox\Profiles\mrcax662.default-release\cache2\entries", "C:\Users\lucas\AppData\Local\Temp", 
"C:\Windows\Temp", "C:\Users\lucas\AppData\Local\Microsoft\Outlook\lehoeltgebaum@furb.br.nst", 
"C:\Users\lucas\AppData\Roaming\Slack\Service Worker\CacheStorage", "C:\Users\lucas\AppData\Roaming\Slack\Cache", 
"C:\Users\lucas\AppData\Roaming\Code\Cache", "C:\Users\lucas\AppData\Roaming\Code\CachedData", 
"C:\Users\lucas\AppData\Roaming\Microsoft\Teams\Service Worker\CacheStorage", "C:\Windows\Downloaded Program Files", 
"C:\Windows\SoftwareDistribution\Download", "C:\Users\lucas\AppData\Local\Microsoft\Windows\Explorer", 
"S:\Documents\Programs\__pycache__", "C:\`$RECYCLE.BIN", "S:\`$RECYCLE.BIN", 
"C:\Program Files (x86)\Microsoft\EdgeCore", "C:\Program Files (x86)\Microsoft\EdgeUpdate",
"C:\Program Files (x86)\Microsoft\EdgeWebView", "C:\Program Files\BsgLauncher\Temp", "C:\Users\lucas\AppData\Local\Microsoft\Teams\previous",
"C:\Users\lucas\AppData\Roaming\discord\Cache")


function RemoveAllFiles() {
    $RemoveSingleFile = {
        param($File)
        # Removes folder in above list
        if (!(Test-Path -Path "$File")) {
            Write-Verbose -Message "Failed to find $File for deletion" -Verbose
            return 0, 0, 0
        }
        Write-Verbose -Message "Attempting to delete $File" -Verbose
        $FolderSize = "{0:N2}" -f ((gci -force -Recurse -ErrorAction SilentlyContinue "$File" | measure Length -ErrorAction SilentlyContinue -s).sum / 1Mb) 
        $Success = Remove-Item -Recurse -Force -Path "$File" -ErrorAction SilentlyContinue
        return $Success, $FolderSize, $File
    }
    $Jobs = @()
    $RemovedFolders = @()
    $TotalSize = 0
    $FolderCount = 0
    foreach ($Folder in $Folders) { 
        $Jobs += Start-Job -ScriptBlock $RemoveSingleFile -ArgumentList $Folder
    }
    foreach ($Job in $Jobs) {
        $FunctionOutput = Wait-Job $Job | Receive-Job
        # Se FunctionOutput[0] == null, houve falha ao remover o arquivo, é então continuado para o próximo arquivo.
        if ($FunctionOutput[0] -eq $null -Or $FunctionOutput[0] -eq 0) {
            Continue
        }
        $FolderCount += 1
        $TotalSize += $FunctionOutput[1]
        $RemovedFolders += $FunctionOutput[2]
    }
    Write-EventLog -LogName "APPLICATION" -Source "Cleanup" -EntryType Information -EventID 4021 -Message "Cleaned $TotalSize MB from Folders below: $RemovedFolders"
    return $FolderCount, $TotalSize
}


function UnninstallEdge {
    # Unninstalls Edge, if it is installed
    $SetupPath = ""
    $EdgePath = "C:\Program Files (x86)\Microsoft\Edge\Application"
    # Verifica se o Path da aplicação do Edge existe e, caso não exista, retorna
    if (!(Test-Path -Path $EdgePath)) {
        Write-Verbose -Message "Did not find Edge at $EdgePath"
        return
    }
    foreach ($Folder in (Get-ChildItem -Path $EdgePath -Directory)) {
        # Regex match para obter folder que o nome é numérico (Folder procurado é o da versão do Edge atualmente instalada)
        if ($Folder.Name.Split(".")[0] -match "^\d+$") {
            $SetupPath = [IO.Path]::Combine($EdgePath, $Folder, "Installer", "setup.exe")
            Write-Verbose -Message "Found Edge Setup Path - $SetupPath"
            break
        }
    }
    # Se o path de Setup do Edge criado préviamente existir, executar o setup com parâmetros para desinstalar
    if (Test-Path -Path $SetupPath) {
        Write-Verbose -Message "Executing Unninstaller for Edge" -Verbose
        & "$SetupPath" --uninstall --system-level --force-uninstall
    }
}

RemoveAllFiles