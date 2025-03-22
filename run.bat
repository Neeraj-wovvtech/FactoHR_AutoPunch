@echo off
cd /d C:\Users\user1\dist\prod-out
call venv\Scripts\activate
python main.py
echo.
echo Script execution completed. Press any key to exit...
pause
