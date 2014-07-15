@ECHO OFF
REM YYYYmmdd_HHMMSS %date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%%time:~6,2%
REM ddmmYYYY_HHMM %date:/=%_%time:~0,2%%time:~3,2%
@ECHO ON
SET filename="~%date:~-4%%date:~3,2%%date:~0,2%_%time:~0,2%%time:~3,2%.txt"
IF DEFINED target_dir ( SET filename="%target_dir:"=%%filename:"=%" ) ELSE (ECHO target_dir is not defined.)
IF NOT DEFINED target_dir ( SET filename="%~dp0%filename:"=%" ) ELSE (ECHO target_dir is defined.)
python "%~dp0parser.py" "vbk ewp ewi pnqi ita eden pgj pbd dfe figy xph cqqq socl ibb feeu eirl" > %filename%
