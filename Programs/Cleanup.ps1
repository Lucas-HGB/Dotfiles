$Folders = "C:\Battlestate Games\EFT\EscapeFromTarkov_Data", "C:\Battlestate Games\BsgLauncher\Temp", "S:\Documents\Default.rdp", "S:\Pictures\Camera Roll", "S:\Pictures\Saved Pictures", "S:\Videos\AnyDesk", "S:\Videos\Captures", "C:\Users\lucas\AppData\Local\Microsoft\Outlook\lucas.hgb2@gmail.com.ost", "C:\Users\lucas\AppData\Local\Microsoft\Outlook\lehoeltgebaum@furb.br.ost", "C:\Users\lucas\AppData\Local\Microsoft\Outlook\lucas.hoeltgebaum@workdb.com.br.nst", "C:\Users\lucas\AppData\Local\Microsoft\Edge", "C:\hiberfil.sys",
"C:\Users\lucas\AppData\Local\Mozilla\Firefox\Profiles\mrcax662.default-release\cache2\entries", "C:\Users\lucas\AppData\Local\Temp", "C:\Windows\Temp",
"C:\Users\lucas\AppData\Local\Microsoft\Outlook\lehoeltgebaum@furb.br.nst", "C:\Users\lucas\AppData\Roaming\Slack\Service Worker\CacheStorage", "C:\Users\lucas\AppData\Roaming\Slack\Cache", "C:\Users\lucas\AppData\Roaming\Code\Cache", "C:\Users\lucas\AppData\Roaming\Code\CachedData", "C:\Users\lucas\AppData\Roaming\Microsoft\Teams\Service Worker\CacheStorage", "C:\Windows\Downloaded Program Files", "C:\Windows\SoftwareDistribution\Download",
"C:\Users\lucas\AppData\Local\Microsoft\Windows\Explorer",
"C:\$Recycle.Bin\S-1-5-21-160320902-3691717267-1884631123-1001"

$totalSize = 0
$folderSize = 0
$folderCount = $Folders.Count
foreach ($Folder in $Folders)
{
	$folderSize = "{0:N2}" -f ((gci -force -Recurse -erroraction 'silentlycontinue' "$Folder" | measure Length -erroraction 'silentlycontinue' -s).sum / 1Gb) 
	$totalSize += $folderSize
    Remove-Item -Recurse -Force -Path "$Folder" -erroraction 'silentlycontinue'
}
#Write-Host "Cleaned Up $totalSize GB from $folderCount"
powershell.exe -WindowStyle hidden -noprofile -File "S:\Documents\Programs\Notification.ps1" "Cleaned Up $totalSize GB from $folderCount Folders"