# =========================================
# Upload Full f4 Folder to GitHub
# =========================================

# -----------------------------
# CONFIGURATION
# -----------------------------
$repoURL = "https://github.com/Snoozzee1027/AttendanceSystemIDSC.git"
$commitMessage = "Upload full f4 folder"
$branchName = "main"

# -----------------------------
# FOLDER TO UPLOAD
# -----------------------------
# The folder containing this script
$folderPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Write-Host "Uploading folder: $folderPath"

# -----------------------------
# FUNCTION: Get ASCII Folder Tree
# -----------------------------
function Get-FolderTree {
    param(
        [string]$path,
        [string]$prefix = ""
    )

    $tree = ""
    $items = Get-ChildItem -Path $path | Sort-Object PSIsContainer, Name
    foreach ($item in $items) {
        if ($item.PSIsContainer) {
            $tree += "$prefix+-- $($item.Name)/`n"
            $tree += Get-FolderTree -path $item.FullName -prefix ($prefix + "|   ")
        } else {
            $tree += "$prefix+-- $($item.Name)`n"
        }
    }
    return $tree
}

$folderTree = Get-FolderTree -path $folderPath
Write-Host "Folder tree generated."

# -----------------------------
# CREATE README.md
# -----------------------------
$readmeContent = @"
# AttendanceSystemIDSC

**Full f4 Folder Upload — Attendance System Project**

---

## Project Structure

$folderTree

---

## Requirements

- Python 3.x
- Packages (if any, see requirements.txt)

---

## Installation & Usage

1. Clone the repository:

git clone $repoURL
cd f4

2. Install dependencies:

pip install -r requirements.txt

3. Run the main program:

python main.py
> Replace 'main.py' with your actual main script if different.

---

## License

This project is for personal or educational use.
"@

# Save README.md in the folder
$readmePath = Join-Path $folderPath "README.md"
$readmeContent | Out-File -FilePath $readmePath -Encoding UTF8
Write-Host "README.md created at $readmePath"

# -----------------------------
# GIT INIT, COMMIT & PUSH
# -----------------------------
# Check if folder is already a git repo
if (-not (Test-Path "$folderPath\.git")) {
    Write-Host "Initializing Git repository..."
    git init $folderPath
} else {
    Write-Host "Git repository already initialized."
}

# Navigate to folder
Set-Location $folderPath

# Add remote if not exists
$remotes = git remote
if ($remotes -notcontains "origin") {
    git remote add origin $repoURL
    Write-Host "Remote 'origin' added."
} else {
    Write-Host "Remote 'origin' already exists."
}

# Stage all files
git add .

# Commit changes
git commit -m "$commitMessage"

# Push to GitHub
git push -u origin $branchName

Write-Host "All files in f4 folder uploaded to GitHub!" -ForegroundColor Green
