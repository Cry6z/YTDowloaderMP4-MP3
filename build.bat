@echo off
REM ===============================
REM Auto build Python ke EXE pakai PyInstaller
REM ===============================

REM Nama file Python utama (ubah sesuai projectmu)
set SCRIPT_NAME=ytdownloader.py

REM Nama icon (hapus --icon kalau ga perlu icon)
set ICON=isntaller.ico

echo 🔨 Building %SCRIPT_NAME% into EXE...
python -m pyinstaller --onefile --icon=%ICON% %SCRIPT_NAME%

echo.
echo ✅ Build selesai! Hasil ada di folder "dist"
pause
