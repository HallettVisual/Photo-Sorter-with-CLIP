@echo off
REM Install dependencies from requirements.txt
pip install -r requirements.txt

REM Inform the user that installation is complete
echo.
echo Installation complete. You can now run the application using:
echo     python photo_sorter.py
pause
