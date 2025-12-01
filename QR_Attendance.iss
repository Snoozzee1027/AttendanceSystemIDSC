[Setup]
AppName=QR Attendance
AppVersion=1.0
DefaultDirName=C:\QR Attendance
DefaultGroupName=QR Attendance
DisableDirPage=yes
AllowNoIcons=yes
OutputDir=Installer
OutputBaseFilename=QR_Attendance_Standalone_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin

[Languages]
Name: "english"
MessagesFile: "compiler:Default.isl"

[Files]
Source: "dist\AttendanceLauncher.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{commondesktop}\QR Attendance"; Filename: "{app}\AttendanceLauncher.exe"; IconFilename: "{app}\assets\icon.ico"
Name: "{group}\QR Attendance"; Filename: "{app}\AttendanceLauncher.exe"; IconFilename: "{app}\assets\icon.ico"
Name: "{commondesktop}\Uninstall QR Attendance"; Filename: "{uninstallexe}"; IconFilename: "{app}\assets\icon.ico"

[Run]
Filename: "{app}\AttendanceLauncher.exe"; Description: "Launch QR Attendance"; Flags: nowait postinstall skipifsilent
