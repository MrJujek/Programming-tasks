# Define the file path
$filePath = "C:\savedDates.txt"

# Check if the file exists
if (-not (Test-Path -Path $filePath)) {
    # Create the file if it doesn't exist
    New-Item -Path $filePath -ItemType File
}

# Get the current date
$currentDate = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Write the current date to the file on a new line
Add-Content -Path $filePath -Value $currentDate
