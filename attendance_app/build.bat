@echo off

::Modern Attendance Launcher Build
::Author: John Gilbert Sevilla


:: 1. Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python 3.10+ and try again.
    pause
    exit /b
)

:: 2. Create virtual environment
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

:: 3. Activate virtual environment
call venv\Scripts\activate.bat

:: 4. Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

:: 5. Install required packages
echo Installing required packages...
pip install --upgrade requests psutil pyinstaller

:: 6. Clean previous builds
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist launcher.spec del /q launcher.spec

:: 7. Build executable with PyInstaller
echo Building standalone executable...
pyinstaller --noconfirm --clean --onefile --windowed launcher.py --name "AttendanceLauncher" --icon static\logo.png

:: 8. Notify user
echo Build completed!
if exist dist\AttendanceLauncher.exe (
    echo Executable created: dist\AttendanceLauncher.exe
    echo Starting the app...
    start "" dist\AttendanceLauncher.exe
) else (
    echo ERROR: Build failed.
)

:: 9. keep console open
pause
