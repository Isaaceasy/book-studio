@echo off
REM Copies the skills and editor agent from "claude-config" into the hidden ".claude" folder that Claude Code reads.
cd /d "%~dp0"
xcopy /E /I /Y "claude-config" ".claude"
if errorlevel 1 (echo Something went wrong.) else (echo Done. You can now delete the claude-config folder. Open Claude Code in this folder and type /new-book)
pause
