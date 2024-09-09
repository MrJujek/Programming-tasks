$service = Get-Service -Name "WazuhSvc" -ErrorAction SilentlyContinue
if ($service -and $service.Status -eq 'Running') {
  Write-Host "WazuhSvc is running."
  exit 0
}
else {
  Write-Host "WazuhSvc is not installed."
}

# Variables
$wazuhInstallerUrl = "https://packages.wazuh.com/4.x/windows/wazuh-agent-4.8.1-1.msi"
$wazuhInstallerPath = "C:\Program Files (x86)\wazuh-agent.msi"
$ossecConfPath = "C:\Program Files (x86)\ossec-agent\ossec.conf"
$managerIp = "192.168.22.21"

# Check if Wazuh installer is installed
if (-not (Test-Path -Path $wazuhInstallerPath)) {
  Write-Host "Downloading Wazuh installer to $wazuhInstallerPath."

  # Download Wazuh installer
  Invoke-WebRequest -Uri $wazuhInstallerUrl -OutFile $wazuhInstallerPath
}
else {
  Write-Host "Wazuh installer already in $wazuhInstallerPath."
}

# Install Wazuh agent
Start-Process msiexec.exe -ArgumentList "/i", `"$wazuhInstallerPath`", "/quiet", "/norestart" -Wait

# Configure ossec.conf
$ossecConfContent = Get-Content $ossecConfPath
$ossecConfContent = $ossecConfContent -replace "<address>.*</address>", "<address>$managerIp</address>"

# Set <localfile> section
$localfileSection = @"
<localfile>
  <location>Microsoft-Windows-Windows Defender/Operational</location>
  <log_format>eventchannel</log_format>
</localfile>
"@

# Check if <localfile> is set
$rawOssecConfContent = Get-Content -Path $ossecConfPath -Raw
if (-not ($rawOssecConfContent -like "*$localfileSection*")) {
  Write-Host "$ossecConfPath is being configured."

  # Add <localfile> to ossec.conf
  $ossecConfContent = $ossecConfContent -replace "</ossec_config>", "$localfileSection`n</ossec_config>"
  $ossecConfContent | Set-Content $ossecConfPath
}
else {
  Write-Host "$ossecConfPath is set."
}

# Check if WazuhSvc is running
if ($service.Status -eq 'Stopped') {
  # Start the service
  Start-Service -Name "WazuhSvc"
  Write-Host "WazuhSvc was stopped and has now been started."
}
else {
  Write-Host "WazuhSvc is already running."
}

# Restart WazuhSvc
Restart-Service -Name "WazuhSvc" -Force
Write-Host "Everything set."

# Read-Host -Prompt "Press Enter to end script"

exit 0