import os
import configparser
from shutil import rmtree, copytree
from time import sleep

config = configparser.ConfigParser()
if not (os.path.isfile('config.ini')):
    print("No config file found!...quit")
    exit()
config.read('config.ini')
print("Config file read successfully...")
sleep(0.5)  # Time in seconds.

if not os.path.isdir(config['PATHS']['terraSysBuildDir']):
    print('Check config.ini: terraSysBuildDir!...quit')
    exit()

print("Copying libs to M drive...")
sleep(0.5)  # Time in seconds.

if config['DEFAULT']['debugOrRelease'] == 'debug':
    destination = config['PATHS']['mDriveFolder'] + '\\' + 'lib_debug'  # config['PATHS']['libDebugDir']
    source = config['PATHS']['terraSysBuildDir'] + '\\' + 'lib_debug'  # config['PATHS']['libDebugDir']
elif config['DEFAULT']['debugOrRelease'] == 'release':
    destination = config['PATHS']['mDriveFolder'] + '\\' + 'lib_release'  # config['PATHS']['libReleaseDir']
    source = config['PATHS']['terraSysBuildDir'] + '\\' + 'lib_release'  # config['PATHS']['libReleaseDir']
else:
    print('Wrong parameters in config.ini...quit')

if os.path.isdir(destination):
    rmtree(destination)
try:
    copytree(source, destination)
except IOError:
    print("Something went wrong. Check config.ini. Read README.txt")
    quit()

print('Libraries copied successfully to M drive')


