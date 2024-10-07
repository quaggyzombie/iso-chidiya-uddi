rem This script aims to set up the project in a local env on windows.
rem Sorry, not sorry linux users, do your own thing.
set PROJECT_DIR=%CD%
if not exist "%PROJECT_DIR%\.venv" (py -3 -m venv .venv)
call ".venv\Scripts\activate"
pip3 install -r requirements.txt
deactivate