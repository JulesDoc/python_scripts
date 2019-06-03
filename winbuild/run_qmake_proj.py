import subprocess
import os
import configparser
import sys
from time import sleep
from shutil import rmtree

# Setting the config python parser
config = configparser.ConfigParser()
if not (os.path.isfile('config.ini')):
    print("No config file found!...quit")
    exit()
config.read('config.ini')
print("Config file read successfully...")
sleep(0.5)  # Time in seconds.

# Checking arguments. Project name is necessary.
if len(sys.argv) < 2:
    print("Missing project name...try again")
    quit()
project = sys.argv[1]

# Setting up files system folders and executing qmake
# System calls are done by means of subprocess module
proFileName = config['PATHS']['terraSysDir'] + '\\' + sys.argv[1] + '\\' + sys.argv[1] + '.pro'
if os.path.isfile(proFileName):
    print("Setting up system...")
    sleep(0.5)  # Time in seconds.
    if os.path.isdir(config['PATHS']['terraSysBuildDir'] + '\\' + sys.argv[1]):
        destination = config['PATHS']['terraSysBuildDir'] + '\\' + sys.argv[1]
        try:
            rmtree(destination)
        except IOError:
            print("Problem removing folder. Removing folder manually")
            try:
                subprocess.run('rd /S /Q ' + destination, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(e.output)
                quit()
        try:
            os.mkdir(destination)
        except subprocess.CalledProcessError as e:
            print("Creating folder manually")
            try:
                subprocess.run('mkdir ' + destination, shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(e.output)
                quit()
    try:
        print("Starting qmake build...")
        sleep(0.5)  # Time in seconds.
        subprocess.run('qmake -tp vc -r -o ' + config['PATHS']['terraSysBuildDir'] + '\\' + sys.argv[1] + ' ' +
                       proFileName, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(e.output)
        quit()
else:
    print("No .pro file found")
    quit()
print("qmake build executed SUCCESSFULLY on " + sys.argv[1] + ' project')




