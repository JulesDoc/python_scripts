# Purpose of these python scripts

	These files are called to substitute batch files used to deploy TerRaSys source code on developer machine. 
Python scripts implements the same functionality as batch files but using 3.7 Python programming language. 


# How to use them

	First thing is execute "settingSystemVars.bat" to set the PATH and QMAKESPEC system variables. This is the only
one batch file remaining, setting an environment variable using a system calls inside a Python script sets it only for 
the current process and any child processes it launches, the best solution is to keep this .bat file.

	Second, configure all the necessary variable in the config.ini file. There is no need to touch any python source code.
Python scripts will read and parse the info written in the config.ini file. To comment a line use '#'.

Then, depending on the necessities of the user:

	- run_qmake_sln: To create terrasys.sln with all projects specified in terrasys.pro.
	
	- run_qmake_proj: To add a new project passed as parameter.


# Advantages of the new approach are:
    - Global location of the configuration variables. All are found in the config.ini file.
    - No need to touch source code.
    - Python is a portable language that could be executed in different platforms, however it is important to bear
    in mind that the scripts may execute system calls only valid under Windows environment (depending on the shell,
    this can be easily modified).
    - Debug or release build is set only once in the config.ini file, then all the scripts will take into account this
    and execute the proper methods.
    - Reduced number of scripts


# Tools settings used for this project

	PyCharm 2018.3.5 (Professional Edition)
	Build #PY-183.5912.18, built on February 26, 2019
	Licensed to PyCharm Evaluator
	Expiration date: March 17, 2019
	JRE: 1.8.0_152-release-1343-b28 amd64
	JVM: OpenJDK 64-Bit Server VM by JetBrains s.r.o
	Windows 10 10.0