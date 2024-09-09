if (Test-Path -Path "$env:USERPROFILE\wazuh-agent.msi") {
  Write-Host "File exists."
}

# Ustawienia
$wazuhInstallerUrl = "https://packages.wazuh.com/4.x/windows/wazuh-agent-4.8.1-1.msi"
$wazuhInstallerPath = "$env:USERPROFILE\wazuh-agent.msi"
$ossecConfPath = "C:\Program Files (x86)\ossec-agent\ossec.conf"
$managerIp = "192.168.22.21"

# Pobierz instalator agenta Wazuh
Invoke-WebRequest -Uri $wazuhInstallerUrl -OutFile $wazuhInstallerPath

# Zainstaluj agenta Wazuh
Start-Process msiexec.exe -ArgumentList "/i", $wazuhInstallerPath, "/quiet", "/norestart" -Wait

# Modyfikacja pliku ossec.conf
$ossecConfContent = Get-Content $ossecConfPath
$ossecConfContent = $ossecConfContent -replace "<address>.*</address>", "<address>$managerIp</address>"

# Dodanie sekcji <localfile>
$localfileSection = @"
<localfile>
  <location>Microsoft-Windows-Windows Defender/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
"@

$ossecConfContent = $ossecConfContent -replace "</ossec_config>", "$localfileSection`n</ossec_config>"
$ossecConfContent | Set-Content $ossecConfPath

# Restart usługi agenta Wazuh
Restart-Service -Name "Wazuh"