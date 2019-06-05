# Purpose of these python scripts

These files are called to substitute batch files used to deploy TerRaSys source code on developer machine.
Also, they are meant to be used to facilitate the integration of the developer code into production.
Python scripts implements the same functionality as batch files but using 3.7 Python programming language.

# System requirements

    1. Install visual studio (Including C++ compiler).
    2. Install Qt. Make sure to have the binaries corresponding to the installed version of visual studio.
        b. Open the file $QT_PATH$\mkspecs\common\msvc-version.conf
        c. Remove all the strings equal to '-Zc:strictStrings'


# Deploy TerRaSys source code on a developer machine

    1. Create a folder in your local machine for the source code. Example: C:\TerRaSysOnTFS
        Note: in this document TERRASYS_DIR refers to the folder where TerRaSys source code is located
    2. Get the latest version from TFS of the files:
        a. TerRaSysOnTFS/dependencies.pro
        b. TerRaSysOnTFS/terrasys.pri
        c. TerRaSysOnTFS/terrasys.pro
        Note: These files contain the configuration existing in the build machine.
    3. Get the latest version of the projects you need to work on. Example: TerRaTronLib

    At this stage you will have the following files hierarchy:

        C:\TerRaSysOnTFS\dependencies.pro
        C:\TerRaSysOnTFS\terrasys.pri
        C:\TerRaSysOnTFS\terrasys.pro
        C:\TerRaSysOnTFS\TerRaTronLib\* (Here are the code source of the project TerRaTronLib)

    4. Edit the file terrasys.pro and change the content as follow (If you are taking only TerRaTronLib):
        Old content:
            SUBDIRS = \
                $$TERRASYS_LIBS \
                $$TERRASYS_PROJECTS

        New content:
            SUBDIRS = \
                TerRaTronLib

        Note: Do not check-in the file terrasys.pro

# Getting python scripts:

    1. Create a folder in your local machine for the projects. Example: C:\TerRaSysBuild
        Note: in this document TERRASYS_BUILD refers to the folder where TerRaSys projects are located

    2. Get the latest version of the scripts from TFS or from GitHub:

        git clone https://github.com/JulesDoc/python_scripts.git

        At this stage you will have the following files hierarchy:

            C:\TerRaSysBuild\settingSystemVars.bat

            C:\TerRaSysBuild\winbuild\run_qmake_sln.py
            C:\TerRaSysBuild\winbuild\run_qmake_proj.py
            C:\TerRaSysBuild\winbuild\config.ini
            C:\TerRaSysBuild\winbuild\README.TXT

            C:\TerRaSysBuild\continuous_build_integration\config.ini
            C:\TerRaSysBuild\continuous_build_integration\copy_3rd_party.py
            C:\TerRaSysBuild\continuous_build_integration\copy_headers_to_m_drive.py
            C:\TerRaSysBuild\continuous_build_integration\qt_deploy.py
            C:\TerRaSysBuild\continuous_build_integration\quick_build.py
            C:\TerRaSysBuild\continuous_build_integration\utils_module.py

    3. Open for editing the file settingSystemVars.bat and modify QMAKESPEC and PATH, save and execute.


# How to use the scripts

Every variable used along these scripts must be defined through the config.ini file. This file implements a basic
configuration language which provides a structure similar to what’s found in Microsoft Windows INI files by means of the
Python Configuration file Parser.

First thing to do is to execute "settingSystemVars.bat" inside winbuild folder(as mentioned before) to set the PATH
and QMAKESPEC system variables. This is the only one batch file remaining from the old configuration.
Setting an environment variable through a system call inside a Python script, sets the variable ONLY for the current
process, thus, the best solution is to keep this .bat file.

Second, as mentioned before, the user needs to configure all necessary variables in the config.ini file.
There is no need to modify any python source code. Python scripts will read and parse the info written in the
config.ini file. To comment a line use '#' + space.

Within the config.ini file, the user can choose between DEBUG or RELEASE build and can also ask to copy libraries and
headers to M drive after the build, those variables are in the DEFAULT part of the file. Config.ini file is very easy to
manage and it does not need more explanations.

****IMPORTANT: Password must be written in the config.ini file to be used ONLY LOCALLY. NEVER CHECK-IN config.file

NOTE on config.ini: There are two files config.ini, one in WINBUILD folder, one in CONTINUOUS_BUILD_INTEGRATION folder.

***DO NOT COMMIT INI FILES***

- DEPLOY SOURCE CODE INTO DEVL MACHINE. WINBUILD FOLDER.

    Following scripts are locate within winbuild folder. Config.ini existing in this folder file will take care of the
    path consistency for the next scripts:

	- run_qmake_sln.py: To create or recreate terrasys.sln with all projects specified in terrasys.pro.
	
	- run_qmake_proj.py: To add a project to the terrasys solution or modify a project passed as parameter.

- BUILD AND INTEGRATE DEVL CODE INTO PRODUCTION. CONTINUOUS_BUILD_INTEGRATION FOLDER.

    Following scripts are located within continuous_build_integration folder.
    Config.ini file existing in this will take care of the path consistency for the next scripts:

    - copy_3rd_party.py: The 3rd party tools should be located in the folder c:\terrasys_3rdparty in the build machine.
    3rd party libraries are used to properly create and execute the projects. This scripts copies every lib or dll
    file into lib_release || lib_debug of the TerRaSysBuild.
    Some of the 3rd_party libs must be configure by the developer: OSGeo4W and prop_mdl_dll_idwm.*. They should be
    present in c:\terrasys_3rdparty when the user execute this script.
    This script can be executed in standalone way or can automatically be called through quick_build.py when working in
    DEBUG or RELEASE mode.

    - copy_headers_to_m_drive.py: When a proper build has been executed, this script copies header files into the M
    drive. This script can be executed in standalone way or can automatically be called through quick_build.py when
    working in DEBUG mode.

    - copy_libs_to_m_drive.py: When a proper build has been executed, this script copies libraries into the M drive.
    This script can be executed in standalone way or can automatically called through quick_build.py when working in
    DEBUG or RELEASE mode.

    - qt_deploy.py: Used mainly to execute windeployqt command to generate and include all the libraries associated with
    a given Qt project to be able to run independently.

    - quick_build.py. Calling this script means mainly build the whole system. It will first copy 3rd party libraries
    and then, it will call DEVENV command to build all VS projects involved. Then, if the build finishes succesfully,
    it will copy libs and headers into M folder. It will also send a mail to the user. In case of successful building,
    the mail will be empty warning that everything went well, in case the build fails, mail will display the name of
    the projects that failed and it will send also, as attached file (outfile.txt) with all the output resulting from the
    build in order to check more precisely, if desired by the user,  where the errors come from.



# Advantages of the new approach are:
    - Global location of the configuration variables. All are found in the config.ini file.
    - No need to touch source code.
    - Python is a portable language that could be executed in different platforms, however, it is important to bear
    in mind that the scripts executes Windows system calls (depending on the shell, this can be easily modified).
    - Debug or release build is set only once in the config.ini file, then, all the scripts will take into account this
    configuration and execute the proper methods.
    - Reduced number of scripts

# Recurrent solutions used over the code

    - subprocess module. Used to launch/execute commands for setting up the folders, copy, delete, etc...
                         Used to execute commands related with the build: devenv, windeployqt.

    - Manually deleting folders using system cmd calls like rd. This due to permission errors on Windows.


# Tools settings used for this project

	PyCharm 2018.3.5 (Professional Edition)
    Build #PY-183.5912.18, built on February 26, 2019
    Student License to Julio Calvo
    Subscription is active until January 17, 2020
    For educational use only.
    JRE: 1.8.0_152-release-1343-b28 x86
    JVM: OpenJDK Server VM by JetBrains s.r.o
    Windows 10 10.0