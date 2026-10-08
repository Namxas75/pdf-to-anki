@echo off
setlocal

set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

if not exist ".venv" (
    py -3 -m venv .venv
)

set VENV_PYTHON=%SCRIPT_DIR%.venv\Scripts\python.exe
"%VENV_PYTHON%" -m pip install --upgrade pip
"%VENV_PYTHON%" -m pip install -r requirements.txt
"%VENV_PYTHON%" -m pip install -e .

"%VENV_PYTHON%" -m pdf_to_anki %*
