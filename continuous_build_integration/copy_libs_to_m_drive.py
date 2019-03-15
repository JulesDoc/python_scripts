import os
import configparser
import subprocess
from shutil import rmtree, copytree
from time import sleep

# Setting up the config python parser
config = configparser.ConfigParser()
if not (os.path.isfile('config.ini')):
    print("No config file found!...quit")
    exit()
config.read('config.ini')
print("Config file read successfully...")
sleep(0.5)  # Time in seconds.

# Checking terraSys path from config.ini
if not os.path.isdir(config['PATHS']['terraSysBuildDir']):
    print('Check config.ini: terraSysBuildDir!...quit')
    exit()

print("Copying libs to M drive...")
sleep(0.5)  # Time in seconds.

# Setting up source and destination. Debug || Release
if config['DEFAULT']['debugOrRelease'] == 'debug':
    destination = config['PATHS']['mDriveFolder'] + '\\' + 'lib'  # config['PATHS']['libDebugDir']
    source = config['PATHS']['terraSysBuildDir'] + '\\' + 'lib'  # config['PATHS']['libDebugDir']
elif config['DEFAULT']['debugOrRelease'] == 'release':
    destination = config['PATHS']['mDriveFolder'] + '\\' + 'lib_release'  # config['PATHS']['libReleaseDir']
    source = config['PATHS']['terraSysBuildDir'] + '\\' + 'lib_release'  # config['PATHS']['libReleaseDir']
else:
    print('Wrong parameters in config.ini...quit')

# and copying libs
if os.path.isdir(destination):
    try:
        rmtree(destination)
    except IOError:
        print("Problem removing include folder. Removing header folder manually")
    try:
        subprocess.run('rd /S /Q ' + destination, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(e.output)
        quit()
try:
    copytree(source, destination)
except IOError:
    print("Something went wrong. Check config.ini. Read README.txt")
    quit()
print('Libraries copied successfully to M drive')


