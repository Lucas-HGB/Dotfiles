# Sources file with Folders List, UnninstallEdge function and RemoveFile function
. src\CleanupFunctions.ps1


function Notify($Title, $Message, $PathToImg) {
	# Notifies User using specifies title, message, and a custom img
	powershell -ExecutionPolicy bypass -command "& { . $PSScriptRoot\src\Notify.ps1; Notify -Title '$Title' -PathToImg '$PathToImg' -Text '$Message' }"
}


function Main {
	# Starts Edge Unninstall as a separate Job, so the rest of the code keeps runing.
	Start-Job -ScriptBlock { UnninstallEdge }
	$TotalSize = 0
	$FolderCount = 0
	foreach ($Folder in $Folders) {if (Test-Path -Path $Folder) {
		$FunctionOutput = RemoveFile $Folder
		# Se FunctionOutput[0] == null, houve falha ao remover o arquivo, é então continuado para o próximo arquivo.
		if ($FunctionOutput[0] -eq $null) {
			Continue
		}
		$TotalSize += $FunctionOutput[1]
		$FolderCount += 1
	}}
	Write-Verbose -Message "Removed $TotalSize MB from $FolderCount Folders"
	Notify -Title "System Cleanup" -Message "Removed $TotalSize MB from $FolderCount Folders" -PathToImg "$PSScriptRoot\src\BroomIcon.png"
}

Main