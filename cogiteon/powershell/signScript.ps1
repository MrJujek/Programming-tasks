param (
    [string]$ScriptPath
)

#Parameters
$CertificateName = "PowerShell Code Signing"
 
#Create a Self-Signed SSL certificate
$Certificate = New-SelfSignedCertificate -CertStoreLocation Cert:\CurrentUser\My -Subject "CN=$CertificateName" -KeySpec Signature -Type CodeSigningCert
 
#Export the Certificate to "Documents" Folder in your computer
$CertificatePath = [Environment]::GetFolderPath("MyDocuments") + "\$CertificateName.cer"
Export-Certificate -Cert $Certificate -FilePath $CertificatePath
 
#Add Certificate to the "Trusted Root Store"
Get-Item $CertificatePath | Import-Certificate -CertStoreLocation "Cert:\LocalMachine\Root"

#Set Parameters
$CertificateThumbprint = $Certificate.Thumbprint
 
#Get the Certificate from Cert Store
$CodeSignCert = Get-ChildItem -Path Cert:\CurrentUser\My | Where-Object { $_.Thumbprint -eq $CertificateThumbprint }
 
#Sign the PS1 file
Set-AuthenticodeSignature -FilePath $ScriptPath -Certificate $CodeSignCert
# SIG # Begin signature block
# MIIFhQYJKoZIhvcNAQcCoIIFdjCCBXICAQExCzAJBgUrDgMCGgUAMGkGCisGAQQB
# gjcCAQSgWzBZMDQGCisGAQQBgjcCAR4wJgIDAQAABBAfzDtgWUsITrck0sYpfvNR
# AgEAAgEAAgEAAgEAAgEAMCEwCQYFKw4DAhoFAAQUS0cwWfiVfhyso+O6vtWiwlVD
# CPKgggMYMIIDFDCCAfygAwIBAgIQH2m3RHZFy6NETcnsrL28jjANBgkqhkiG9w0B
# AQUFADAiMSAwHgYDVQQDDBdQb3dlclNoZWxsIENvZGUgU2lnbmluZzAeFw0yNDA5
# MDUwNjM3MTVaFw0yNTA5MDUwNjU3MTVaMCIxIDAeBgNVBAMMF1Bvd2VyU2hlbGwg
# Q29kZSBTaWduaW5nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyYsd
# tgOcrZHl2eq18sgjMuSO6zp8ytCCoYzKAR23AzVXun61h1b2utjWQZAD1ot//cOP
# gG2j5hQTbWa+MZG1CmPY2ZstXjB4SpRH+wEP/vIO4BodXH1hySpw8o4jkrBLi67z
# JyMWZLCo0cCahO0nt5ivAjcIXzjn+6DqXdX4lwL0tAN9AU1MRLUPoErxoXc2vPG6
# OM0SrGAdA4tYlKkTeJx22nG4CGYM2EfFr36FWwVA5r6DiUh650u5HGSOpGQ18V7l
# nvfg6B7SUcoQRBSj6q2H63RrVd2Z/9mh0UIWs+mv8yHf7u2iDIPFJWB/5T3U5/t1
# mVRk/mW2aaB5y9rWRQIDAQABo0YwRDAOBgNVHQ8BAf8EBAMCB4AwEwYDVR0lBAww
# CgYIKwYBBQUHAwMwHQYDVR0OBBYEFAttTqt21Od6DTAbKArD8iJH21WeMA0GCSqG
# SIb3DQEBBQUAA4IBAQDElb3V+IDfelNBAEzlosLfN4m4hLFnoR9LQp5rm6AVzg5h
# fVIDXUOifSbg1wPcsrHwffqz24+fiRd+b43H/QD9dnqLg9rFPDSPmvq0yIoa6jU5
# 10NnoCrEockCqCg9vDqg3OBn2IlK9fJXKRG+xf7b/hrkEsRnwnTWHPpPSE/7Er4d
# By/A6NPdS82Zorg45CyKsDeZH30W1LSE1tVxZ6LUez3nJfipN61++EtJ7YStpJ+F
# yBCKdRF7bmorhXQP20KasdUJ2bAz/JDJd3LmXT7UCbb9IMcM2QRZkr6kbqfo9ze2
# rHkbdjhNxl40o6W8pYvjWbjuC7vS77ABOb80Zk8sMYIB1zCCAdMCAQEwNjAiMSAw
# HgYDVQQDDBdQb3dlclNoZWxsIENvZGUgU2lnbmluZwIQH2m3RHZFy6NETcnsrL28
# jjAJBgUrDgMCGgUAoHgwGAYKKwYBBAGCNwIBDDEKMAigAoAAoQKAADAZBgkqhkiG
# 9w0BCQMxDAYKKwYBBAGCNwIBBDAcBgorBgEEAYI3AgELMQ4wDAYKKwYBBAGCNwIB
# FTAjBgkqhkiG9w0BCQQxFgQUVjqS4vvKEqUxklzmh7rY/01sDRgwDQYJKoZIhvcN
# AQEBBQAEggEAeDs8hbytmv4tRS/z6826zU2EU/kPxhzcg4e8n5z0SVXvVG3rH6hQ
# e3wEV6IzpffdgEgzdeyOLST+ETrM+lzsxTp3uDQ9ugdIK4+fDLh7XvtwZjrciaeB
# o/aQXJYCSQ1ryN3RtQXO7BR+t4iMrqCY7vThcrPZfuHBiPBBiT0Gx9Gg5esPSuSM
# JKkAbKwW7+kZ1ZDRLVAwe3E7a/HL6zJj4pZWOJ9ueAIW/wDdO9tz7MvuZfrk+ACG
# Bhh+T6ml1sHEvG9+m+KOoEFn93iXcTiaM79KONpcQ5RoP2DEzhGsMBdU/Xqd5jE6
# U1YpZAttWdVFhmDANODsfHuBWZ6NpXUHEQ==
# SIG # End signature block
