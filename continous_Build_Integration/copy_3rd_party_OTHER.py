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

# First part of the script used to copy libs from 3rd party folders to C:\terrasys_3rdparty
# Setting up destination and source for idwm32d.dll copy
# source = config['PATHS']['idwmFilesPath'] + '\\' + config['PATHS']['idwmDllFile']
# if not os.path.isfile(source):
#    print("Check config file: idwmFilesPath/idwmDllFile")
#     exit()
# if os.path.isfile(destination + '\\' + config['PATHS']['idwmDllFile']):
#    subprocess.run('del /f ' + destination + '\\' + config['PATHS']['idwmDllFile'], shell=True)
#try:
#    copy(source, destination)
#except IOError:
#    print("Something went wrong. Check config.ini. Read README.txt")
#    quit()

# First part of the script used to copy libs from 3rd party folders to C:\terrasys_3rdparty
# For idwm32d.lib
# source = config['PATHS']['idwmFilesPath'] + '\\' + config['PATHS']['idwmLibFile']
# if not os.path.isfile(source):
#   print("Check config file: idwmFilesPath/idwmLibFile")
#    exit()
#if os.path.isfile(destination + '\\' + config['PATHS']['idwmLibFile']):
#    subprocess.run('del /f ' + destination + '\\' + config['PATHS']['idwmLibFile'], shell=True)
#try:
#    copy(source, destination)
#except IOError:
#    print("Something went wrong. Check config.ini. Read README.txt")
#    quit()

lista_folder = [config['PATHS']['idwmLibFile'], config['PATHS']['idwmDllFile'], config['PATHS']['osGeo4wBin'],
                config['PATHS']['osGeo4wLib'], config['PATHS']['osGeo4wShare'], config['PATHS']['osGeo4wInclude'],
                config['PATHS']['bcdLibFile'], config['PATHS']['bcdDllFile']]
for folder in lista_folder:
    source = folder
    # if os.path.isfile(source):
    #    subprocess.run('del /f ' + destination, shell=True)
    #    copy(source, destination)
    # elif os.path.isdir(source):
    #    subprocess.run('rd /S /Q ' + destination, shell=True, check=True)
    #    copytree(source, destination)
    utils_module.recursive_overwrite(source, destination)
# Second part. Copyinf from 3rd pary folder to lib_debug / lib_release
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
    utils_module.recursive_overwrite(source, destination)
    #src_files = os.listdir(source)
    #for file_name in src_files:
    #    if file_name.endswith('.dll') or file_name.endswith('lib'):
    #        if os.path.isfile(destination + '\\' + file_name):
    #            subprocess.run('del /f ' + destination + '\\' + file_name, shell=True)
    #        try:
    #            copy(source + '\\' + file_name, destination)
    #        except IOError:
    #            print("Something went wrong. Check config.ini. Read README.txt")
    #            quit()

    # Copy Qt libraries
    print("Copying Qt libraries for release...")
    sleep(0.5)  # Time in seconds.
    destination = config['PATHS']['libReleaseDir']
    source = config['PATHS']['qtDeployReleaseDir']
    utils_module.recursive_overwrite(source, destination)
else:
    print('Wrong parameters in config.ini...quit')
print('3rd Party Copying finished successfully')
