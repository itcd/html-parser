@ECHO OFF
REM Echo Launch dir: "%~dp0"
REM Echo Current dir: "%CD%"
@ECHO ON
SET target_dir="%~dp0..\"
call "%~dp0run.bat"
