
function CreateService($Name, $PathToExecutable, $DisplayName, $StartupType="Automatic", $Description="") {
  $params = @{
    Name = "$Name"
    BinaryPathName = "$PathToExecutable"
    DisplayName = "$DisplayName"
    StartupType = "$StartupType"
    Description = "$Description"
  }
  New-Service @params
}
