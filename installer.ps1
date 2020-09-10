$python = (Get-Command pythonw).path
$cwd = (Get-Item .).FullName
$script = (Get-Item main.py).FullName
$startupFolder = "$env:ALLUSERSPROFILE\Microsoft\Windows\Start Menu\Programs\StartUp"

$msg = "
Options
    -i : install
    -u : uninstall
    -h : help
"

if ($args.Count -eq 1) {
    switch ($args[0]) {
        "-i" {
            # creates a startup shortcut
            $WshShell = New-Object -ComObject WScript.Shell
            $shortCut = $WshShell.CreateShortcut("$startupFolder\Meetings Assistant.lnk")
            $shortCut.TargetPath = $python
            $shortCut.Arguments = $script
            $shortCut.WorkingDirectory = $cwd
            $shortCut.Save()
            Start-Process "$startupFolder\Meetings Assistant.lnk"
            Break
        }
        "-u" {
            # deletes the startup shortcut
            Remove-Item -Path "$startupFolder\Meetings Assistant.lnk"
            Break
        }
        "-h" {
            Write-Output $msg
            Break
        }
        Default {
            Write-Output $msg $cwd
        }
    }

}
else {
    Write-Output $msg
}
