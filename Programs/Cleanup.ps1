$Folders = "S:\Documents\Default.rdp", "S:\Pictures\Camera Roll", "S:\Pictures\Saved Pictures", "S:\Videos\AnyDesk", "S:\Videos\Captures", "C:\Users\lucas\AppData\Local\Microsoft\Outlook\lucas.hgb2@gmail.com.ost", "C:\Users\lucas\AppData\Local\Microsoft\Outlook\lehoeltgebaum@furb.br.ost", "C:\Users\lucas\AppData\Local\Microsoft\Outlook\lucas.hoeltgebaum@workdb.com.br.nst", "C:\Users\lucas\AppData\Local\Microsoft\Edge", "C:\hiberfil.sys",
"C:\Users\lucas\AppData\Local\Mozilla\Firefox\Profiles\mrcax662.default-release\cache2\entries", "C:\Users\lucas\AppData\Local\Temp", "C:\Windows\Temp",
"C:\Users\lucas\AppData\Local\Microsoft\Outlook\lehoeltgebaum@furb.br.nst", "C:\Users\lucas\AppData\Roaming\Slack\Service Worker\CacheStorage", "C:\Users\lucas\AppData\Roaming\Slack\Cache", "C:\Users\lucas\AppData\Roaming\Code\Cache", "C:\Users\lucas\AppData\Roaming\Code\CachedData", "C:\Users\lucas\AppData\Roaming\Microsoft\Teams\Service Worker\CacheStorage", "C:\Windows\Downloaded Program Files", "C:\Windows\SoftwareDistribution\Download",
"C:\Users\lucas\AppData\Local\Microsoft\Windows\Explorer",
"S:\Documents\Programs\__pycache__", "C:\`$RECYCLE.BIN", "S:\`$RECYCLE.BIN"

$totalSize = 0
$folderCount = 0
foreach ($Folder in $Folders) {if (Test-Path -Path $Folder) {
	$folderSize = "{0:N2}" -f ((gci -force -Recurse -erroraction 'silentlycontinue' "$Folder" | measure Length -erroraction 'silentlycontinue' -s).sum / 1Gb) 
	$totalSize += $folderSize
	$folderCount += 1
	Remove-Item -Recurse -Force -Path "$Folder" -erroraction 'silentlycontinue'
}}

powershell -ExecutionPolicy bypass -command "& { . S:\Documents\Programs\Notify.ps1; Notify -Title 'System Cleanup' -PathToImg '$PSScriptRoot\BroomIcon.png' -Text 'Removed $totalSize GB from $folderCount Folders' }"
