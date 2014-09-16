@ECHO OFF
REM YYYYmmdd_HHMMSS %date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%%time:~6,2%
REM ddmmYYYY_HHMM %date:/=%_%time:~0,2%%time:~3,2%
@ECHO ON
SET time_str="~%date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%_%time:~6,2%.txt"
IF DEFINED target_dir ( SET filename="%target_dir:"=%%time_str:"=%" )
IF NOT DEFINED target_dir ( SET filename="%~dp0%time_str:"=%" )
python "%~dp0parser.py" "dfe ivv blv ewp ijh mlpx qqq vbk soxx eden zroz xph cqqq xiv pgj kweb" > %filename%
