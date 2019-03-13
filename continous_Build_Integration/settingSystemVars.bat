@echo off

set QMAKESPEC=win32-msvc
title %QMAKESPEC% Qt5.12.1
set PATH=%QT_DIR%\bin;%PATH%
CALL "C:\Program Files (x86)\Microsoft Visual Studio\2017\Professional\VC\Auxiliary\Build\vcvarsall.bat" x86
echo System variables set up successfully
echo DONE

:endFile