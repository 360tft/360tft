@echo off
REM 360TFT Weekly Content Automation - Windows Batch Script
REM Helps run the automation system on Windows

echo ================================
echo 360TFT WEEKLY CONTENT AUTOMATION
echo ================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found! Please install Python 3.7+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found! Running integration tests...
echo.

REM Run integration tests
python test_integration.py

echo.
echo Integration tests complete.
echo.

:menu
echo What would you like to do?
echo 1. Run complete week manually (recommended for first time)
echo 2. Check current progress status
echo 3. Start automated scheduling
echo 4. Test topic selection
echo 5. Install required packages
echo 6. Exit
echo.
set /p choice=Enter your choice (1-6): 

if "%choice%"=="1" goto run_week
if "%choice%"=="2" goto check_status
if "%choice%"=="3" goto start_schedule
if "%choice%"=="4" goto test_topics
if "%choice%"=="5" goto install_packages
if "%choice%"=="6" goto end

echo Invalid choice. Please try again.
goto menu

:run_week
echo.
echo Running complete week's content creation...
echo This will take several minutes. Please wait...
echo.
python Weekly_Content_Automation.py run-week
echo.
echo Week execution complete! Check the results above.
pause
goto menu

:check_status
echo.
echo Checking current automation status...
echo.
python Weekly_Content_Automation.py status
echo.
pause
goto menu

:start_schedule
echo.
echo Starting automated weekly scheduling...
echo WARNING: This will run continuously. Press Ctrl+C to stop.
echo.
set /p confirm=Are you sure you want to start automated scheduling? (y/n): 
if /i "%confirm%"=="y" (
    python Weekly_Content_Automation.py schedule
) else (
    echo Cancelled.
)
goto menu

:test_topics
echo.
echo Testing topic selection system...
echo.
python Topic_Selection_Manager.py report
echo.
pause
goto menu

:install_packages
echo.
echo Installing required Python packages...
echo.
pip install -r requirements.txt
echo.
echo Package installation complete!
pause
goto menu

:end
echo.
echo Thank you for using 360TFT Weekly Content Automation!
echo.
pause