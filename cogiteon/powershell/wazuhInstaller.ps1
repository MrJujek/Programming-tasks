# Variables
$wazuhInstallerUrl = "https://packages.wazuh.com/4.x/windows/wazuh-agent-4.8.1-1.msi"
$wazuhInstallerPath = "$env:USERPROFILE\wazuh-agent.msi"
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
Start-Process msiexec.exe -ArgumentList "/i", $wazuhInstallerPath, "/quiet", "/norestart" -Wait

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

# Restart Wazuh agent
Restart-Service -Name "Wazuh"

# Write-Host "Press Enter to end script."
# Read-Host
# SIG # Begin signature block
# MIIFhQYJKoZIhvcNAQcCoIIFdjCCBXICAQExCzAJBgUrDgMCGgUAMGkGCisGAQQB
# gjcCAQSgWzBZMDQGCisGAQQBgjcCAR4wJgIDAQAABBAfzDtgWUsITrck0sYpfvNR
# AgEAAgEAAgEAAgEAAgEAMCEwCQYFKw4DAhoFAAQUfAZWfp8DIDWCrzBcm1Th7xdq
# XZWgggMYMIIDFDCCAfygAwIBAgIQTgCwgfSO0IdGnQoEg5qC3TANBgkqhkiG9w0B
# AQUFADAiMSAwHgYDVQQDDBdQb3dlclNoZWxsIENvZGUgU2lnbmluZzAeFw0yNDA5
# MDYxMDI0MzBaFw0yNTA5MDYxMDQ0MzBaMCIxIDAeBgNVBAMMF1Bvd2VyU2hlbGwg
# Q29kZSBTaWduaW5nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzlER
# iqrZt2fdIw3V7BMJ7KZtpqIKauFxUpfG00j67pTpWOK0BjBrQWD5z9PWBygtP6F8
# 3FsNJSgJdbXYu+7kA162uOWSlk/oR55ImSHW98l03X2js+2H3JyaHuQ8n3NcFZSj
# 2M/1qtt9VWokrTxUmacY6eZOfFYVOoQJikcgdkSEq//nx/uPgx0WSEJArL0ySD+y
# sF9Xqq9Tw23cLEFx4DNj59hwtEnOuPwbCcdjaeJFvuKX6bE2omk6RCu5o58A8jXE
# 6gMw9dMp3y7mAOdPZNTiL6cLkiquyz+xC8i0xaMDBE1Fj3jmdEQ38oeW30omjj5C
# YL3UK1Q11UMZ3WEdqQIDAQABo0YwRDAOBgNVHQ8BAf8EBAMCB4AwEwYDVR0lBAww
# CgYIKwYBBQUHAwMwHQYDVR0OBBYEFOmuQozZ9FGWLORnK+C1XwfK9KJoMA0GCSqG
# SIb3DQEBBQUAA4IBAQCbXHItS3Y43n7/BP/udN+wKFWi2tizh+ApUqrydwA3W4H/
# bZ/5k3pvuyXw84QZKkIH3OycxmqwPCr3If+ZfsuJ1NKTtVbbxZ/BucNXpKVrk2LD
# zvzqKxM2veQ7w3FZGRKeUr7Rfxix4+OynjBYs0NOa/rppImGLBNgjWVkbWIlaORE
# 3iTT1rXh/wMAC3T6ZzGXpJ7GRu2JWftmDJcwZ1d3+zBXiv9ku/hsxfSlEWly4A6A
# sFJgTgp12f4EpINftKr3nGL3pWCyWiMb2DTspCQoyCmuPowdWCf+B/vHpbN47dUi
# Gl0uzWm9lKMrx+XGBPmTZOTgmhvEh8XS9vUNOTkUMYIB1zCCAdMCAQEwNjAiMSAw
# HgYDVQQDDBdQb3dlclNoZWxsIENvZGUgU2lnbmluZwIQTgCwgfSO0IdGnQoEg5qC
# 3TAJBgUrDgMCGgUAoHgwGAYKKwYBBAGCNwIBDDEKMAigAoAAoQKAADAZBgkqhkiG
# 9w0BCQMxDAYKKwYBBAGCNwIBBDAcBgorBgEEAYI3AgELMQ4wDAYKKwYBBAGCNwIB
# FTAjBgkqhkiG9w0BCQQxFgQU7L9YRvVRi42oQiDCmoxnHjNZJkQwDQYJKoZIhvcN
# AQEBBQAEggEAZ1j08FdWnA4P63u+Ob49K5aWNSZ6bQcHNUMClMHMV1hHT0jVCbGu
# 9NlS/ub5k/jWgp6+5mo0N7H0BXyfL/B3yEDfeLGcIRQAlt6JE2fJANcF85Ecy0ZP
# 3XbAwN+3iRxkUf7CvCjPfDQ+XObJ+vKcJWH22aiAJZlCt1/A8xvOmY2zKs4iP4rW
# YS+7RruNKelOZXlqe0wIRwT9omt6oCtObznadiIsJy/5egUlLuRKDF1sp4xeHfzY
# DkdJlsu5HJhQAWnnjI7UUKIgOelmDn5wMh/sFZhFXSaKFcuwadoVnZ09TkFTGsxK
# AHqRTPkdrAaAv1pRMFG7wB7JjIDD8zr1aw==
# SIG # End signature block
