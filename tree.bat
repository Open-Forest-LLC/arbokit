@echo off
chcp 65001 >nul
powershell -ExecutionPolicy Bypass -File "%~dp0tree.ps1" -StartPath "."
pause