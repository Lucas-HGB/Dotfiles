Add-Type @"
  using System;
  using System.Runtime.InteropServices;
  public class Tricks {
    [DllImport("user32.dll")]
    public static extern IntPtr GetForegroundWindow();
}
"@

$a = [tricks]::GetForegroundWindow()

$WH = get-process | ? { $_.mainwindowhandle -eq $a }
$activePID = $WH.ID
Stop-Process -Force -ID $activePID
