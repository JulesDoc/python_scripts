import os
import configparser
from time import sleep
import subprocess
import utils_module
from shutil import copy, copytree

# Setting the config python parser
config = configparser.ConfigParser()
if not (os.path.isfile('config.ini')):
    print('No config file found!...quit')
    exit()
config.read('config.ini')
print("Config file read successfully...")
sleep(0.5)  # Time in seconds.

# Setting up destination for 3rdParty folder
destination = config['PATHS']['3rdPartyDir']
if not os.path.isdir(destination):
    print("Check config file: 3rdPartyDir")
    exit()
print("Copying IDWM files from M to 3rdPartyDir...")

# First part of the script used to copy IDWM libs to C:\terrasys_3rdparty
# Setting up source for idwm32d copy
path_idwm = config['PATHS']['idwmFilesPath']
lista_files = [config['PATHS']['idwmLibFile'], config['PATHS']['idwmDllFile']]
for file in lista_files:
    source = os.path.join(path_idwm, file)
    if os.path.isfile(source):
        subprocess.run('del /f ' + os.path.join(destination, file), shell=True)
        try:
            copy(source, destination)
        except IOError:
            print("Something went wrong. Check config.ini. Read README.txt")
            quit()
    else:
        print("Check config file: idwmFilesPath")

# Second part. Copying from 3rd party folder files to lib_debug / lib_release
# Setting up source and destination for copying .dll and .libs in Debug
if config['DEFAULT']['debugOrRelease'] == 'debug':

    # Copy 3rd party libraries
    # Copying *.dll or *.lib files
    print("Copying 3rd party libraries (.dll & . lib) for debug...")
    sleep(0.5)  # Time in seconds.
    destination = config['PATHS']['libDebugDir']
    source = config['PATHS']['3rdPartyDir']
    src_files = os.listdir(source)
    for file_name in src_files:
        if file_name.endswith('.dll') or file_name.endswith('lib'):
            if os.path.isfile(destination + '\\' + file_name):
                subprocess.run('del /f ' + destination + '\\' + file_name, shell=True)
            try:
                copy(source + '\\' + file_name, destination)
            except IOError:
                print("Something went wrong. Check config.ini. Read README.txt")
                quit()

    # Copy Qt libraries
    print("Copying Qt libraries for debug...")
    sleep(0.5)  # Time in seconds.
    destination = config['PATHS']['libDebugDir']
    source = config['PATHS']['qtDeployDebugDir']
    utils_module.recursive_overwrite(source, destination)

# Setting up source and destination for copying .dll and .libs in Release
elif config['DEFAULT']['debugOrRelease'] == 'release':

    # Copy 3rd party libraries
    # Copying *.dll or *.lib files
    print("Copying 3rd party libraries (.dll & . lib) for release...")
    sleep(0.5)  # Time in seconds.
    destination = config['PATHS']['libReleaseDir']
    source = config['PATHS']['3rdPartyDir']
    src_files = os.listdir(source)
    for file_name in src_files:
        if file_name.endswith('.dll') or file_name.endswith('lib'):
            if os.path.isfile(destination + '\\' + file_name):
                subprocess.run('del /f ' + destination + '\\' + file_name, shell=True)
            try:
                copy(source + '\\' + file_name, destination)
            except IOError:
                print("Something went wrong. Check config.ini. Read README.txt")
                quit()

    # Copy Qt libraries
    print("Copying Qt libraries for release...")
    sleep(0.5)  # Time in seconds.
    destination = config['PATHS']['libReleaseDir']
    source = config['PATHS']['qtDeployReleaseDir']
    utils_module.recursive_overwrite(source, destination)
else:
    print('Wrong parameters in config.ini...quit')
print('3rd Party Copying finished successfully')
