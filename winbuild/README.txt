# Purpose of these python scripts

These files are called to substitute batch files used to deploy TerRaSys source code on developer machine.
And also are meant to be used to facilitate the integration of the developer code into production.
Python scripts implements the same functionality as batch files but using 3.7 Python programming language. 


# How to use them

Every variable used along these scripts must be defined through the config.ini file. This file implements a basic
configuration language which provides a structure similar to what’s found in Microsoft Windows INI files by means of the
Python Configuration file Parser.

First thing to do is to execute "settingSystemVars.bat" to set the PATH and QMAKESPEC system variables. This is the only
one batch file remaining because setting an environment variable through a system calls inside a Python script sets it only for
the current process and any child processes it launches, thus, the best solution is to keep this .bat file.

Second, as mentioned before, the user needs to configure all necessary variables in the config.ini file.
There is no need to modify any python source code. Python scripts will read and parse the info written in the
config.ini file. To comment a line use '#' + space.

DEPLOY SOURCE CODE INTO DEVL MACHINE: Depending on the necessities of the user:

	- run_qmake_sln: To create terrasys.sln with all projects specified in terrasys.pro.
	
	- run_qmake_proj: To add a new project passed as parameter.

BUILD AND INTEGRATE DEVL CODE INTO PRODUCTION:

    - copy_3rd_party.py: The 3rd party tools should be located in the folder c:\terrasys_3rdparty in the build machine.
    This 3rd party libraries are used to properly create and execute the projects.

    - copy_headers_to_m_drive.py:

    - copy_libs_to_m_drive.py:

    - qt_deploy.py



# Advantages of the new approach are:
    - Global location of the configuration variables. All are found in the config.ini file.
    - No need to touch source code.
    - Python is a portable language that could be executed in different platforms, however it is important to bear
    in mind that the scripts may execute system calls only valid under Windows environment (depending on the shell,
    this can be easily modified).
    - Debug or release build is set only once in the config.ini file, then all the scripts will take into account this
    and execute the proper methods.
    - Reduced number of scripts

# Recurrent solutions used over the code

    - subprocess module. Used to launch/execute commands for setting up the folders, copy, delete, etc...
                         Used to execute commands related with the build: devenv, windeploy.

    - Manually deleting folders using system cmd calls like rd. This due to permission errors on Windows.


# Tools settings used for this project

	PyCharm 2018.3.5 (Professional Edition)
	Build #PY-183.5912.18, built on February 26, 2019
	Licensed to PyCharm Evaluator
	Expiration date: March 17, 2019
	JRE: 1.8.0_152-release-1343-b28 amd64
	JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
	Windows 10 10.0