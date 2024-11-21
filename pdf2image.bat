@echo off

if "%1" == "" (
    echo Usage: pdf2image.bat ^<src_dir^> [^<dest_dir^>]
    exit /b 1
)

set SRC_DIR=%~f1
set DEST_DIR=%~f2

for /R "%SRC_DIR%" %%I in ( *.pdf ) do (
    echo Converting file: %%I
    if "%DEST_DIR%" == "" (
        "%~dp0\pdf2image.exe" --dpi 144 "%%I"
    ) else (
        "%~dp0\pdf2image.exe" --dpi 144 --outdir "%DEST_DIR%\%%~nI" "%%I"
    )
)
