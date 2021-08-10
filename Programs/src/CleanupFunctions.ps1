$Folders = "S:\Documents\Default.rdp", "S:\Pictures\Camera Roll", "S:\Pictures\Saved Pictures", "S:\Videos\AnyDesk", 
"S:\Videos\Captures", "C:\Users\lucas\AppData\Local\Microsoft\Edge", "C:\hiberfil.sys", 
"C:\Users\lucas\AppData\Local\Mozilla\Firefox\Profiles\mrcax662.default-release\cache2\entries", "C:\Users\lucas\AppData\Local\Temp", 
"C:\Windows\Temp", "C:\Users\lucas\AppData\Local\Microsoft\Outlook\lehoeltgebaum@furb.br.nst", 
"C:\Users\lucas\AppData\Roaming\Slack\Service Worker\CacheStorage", "C:\Users\lucas\AppData\Roaming\Slack\Cache", 
"C:\Users\lucas\AppData\Roaming\Code\Cache", "C:\Users\lucas\AppData\Roaming\Code\CachedData", 
"C:\Users\lucas\AppData\Roaming\Microsoft\Teams\Service Worker\CacheStorage", "C:\Windows\Downloaded Program Files", 
"C:\Windows\SoftwareDistribution\Download", "C:\Users\lucas\AppData\Local\Microsoft\Windows\Explorer", 
"S:\Documents\Programs\__pycache__", "C:\`$RECYCLE.BIN", "S:\`$RECYCLE.BIN", 
"C:\Program Files (x86)\Microsoft\EdgeCore", "C:\Program Files (x86)\Microsoft\EdgeUpdate",
"C:\Program Files (x86)\Microsoft\EdgeWebView"

function RemoveFile($File) {
    # Removes folder in above list
    Write-Verbose -Message "Attempting to delete $Folder"
    $FolderSize = "{0:N2}" -f ((gci -force -Recurse -ErrorAction 'silentlycontinue' "$Folder" | measure Length -ErrorAction 'silentlycontinue' -s).sum / 1Mb) 
    $Success = Remove-Item -Recurse -Force -Path "$Folder" -ErrorAction 'silentlycontinue'
    return $Success, $FolderSize   
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
        Write-Verbose -Message "Executing Unninstaller for Edge"
        & "$SetupPath" --uninstall --system-level --force-uninstall
    }
}