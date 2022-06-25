Set oShell = CreateObject("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c bPassword.bat"
oShell.Run strArgs, 0, false