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
if not os.path.isdir(config['PATHS']['terraSysDir']):
    print('Check config.ini: terraSysDir!...quit')
    exit()

print("Copying headers to M drive...")
sleep(0.5)  # Time in seconds.

# Setting up source and destination and copying headers
for dir_name in os.listdir(config['PATHS']['terraSysDir']):
    if os.path.isdir(config['PATHS']['terraSysDir'] + '\\' + dir_name + '\\' + 'include'):
        source = config['PATHS']['terraSysDir'] + '\\' + dir_name + '\\' + 'include'
        destination = config['PATHS']['mDriveFolderHeaders'] + '\\' + dir_name + '\\' + 'include'
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
print('Headers copied successfully to M drive')
