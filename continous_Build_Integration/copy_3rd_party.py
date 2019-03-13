import os
import configparser
from time import sleep
import subprocess
from shutil import copy, copyfile


def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f),
                                    os.path.join(dest, f),
                                    ignore)
    else:
        copyfile(src, dest)


config = configparser.ConfigParser()
if not (os.path.isfile('config.ini')):
    print('No config file found!...quit')
    exit()
config.read('config.ini')
print("Config file read successfully...")
sleep(0.5)  # Time in seconds.

destination = config['PATHS']['3rdPartyDir']
if not os.path.isdir(destination):
    print("Check config file: 3rdPartyDir")
    exit()
print("Copying IDWM files from M to 3rdPartyDir...")
# idwm32d.dll
source = config['PATHS']['idwmFilesPath'] + '\\' + config['PATHS']['idwmDllFile']
if not os.path.isfile(source):
    print("Check config file: idwmFilesPath/idwmDllFile")
    exit()
if os.path.isfile(destination + '\\' + config['PATHS']['idwmDllFile']):
    subprocess.run('del /f ' + destination + '\\' + config['PATHS']['idwmDllFile'], shell=True)
try:
    copy(source, destination + '\\' + config['PATHS']['idwmDllFile'])
except IOError:
    print("Something went wrong. Check config.ini. Read README.txt")
    quit()
# idwm32d.lib
source = config['PATHS']['idwmFilesPath'] + '\\' + config['PATHS']['idwmLibFile']
if not os.path.isfile(source):
    print("Check config file: idwmFilesPath/idwmLibFile")
    exit()
if os.path.isfile(destination + '\\' + config['PATHS']['idwmLibFile']):
    subprocess.run('del /f ' + destination + '\\' + config['PATHS']['idwmLibFile'], shell=True)
try:
    copy(source, destination)
except IOError:
    print("Something went wrong. Check config.ini. Read README.txt")
    quit()

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
    recursive_overwrite(source, destination)
    # copytree(source, destination)

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
    recursive_overwrite(source, destination)
else:
    print('Wrong parameters in config.ini...quit')
print('3rd Party Copying finished successfully')
