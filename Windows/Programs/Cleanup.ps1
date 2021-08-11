# Sources file with Folders List, UnninstallEdge function and RemoveAllFiles function
. src\CleanupFunctions.ps1


function Notify($Title, $Message, $PathToImg) {
	# Notifies User using specifies title, message, and a custom img
	powershell -ExecutionPolicy bypass -command "& { . $PSScriptRoot\src\Notify.ps1; Notify -Title '$Title' -PathToImg '$PathToImg' -Text '$Message' }"
}


function Main {
	# Starts Edge Unninstall as a separate Job, so the rest of the code keeps runing.
	Start-Job -ScriptBlock { UnninstallEdge }
	$FolderCount, $TotalSize = RemoveAllFiles
	Write-Verbose -Message "Removed $TotalSize MB from $FolderCount Folders" -Verbose
	Notify -Title "System Cleanup" -Message "Removed $TotalSize MB from $FolderCount Folders" -PathToImg "$PSScriptRoot\src\BroomIcon.png"
}

Main