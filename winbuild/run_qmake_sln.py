import subprocess
import os
import configparser
from time import sleep

config = configparser.ConfigParser()
if not (os.path.isfile('config.ini')):
    print('')
    print("No config file found!...quit")
    exit()
config.read('config.ini')
print("Config file read successfully...")
sleep(0.5)  # Time in seconds.
try:
    print("Starting qmake build...")
    sleep(0.5)  # Time in seconds.
    return_value = subprocess.run('qmake -tp vc -r -o ' + config['PATHS']['terraSysBuildDir'] + ' '
                                  + config['PATHS']['terraSysDir'] + '\\' + 'terrasys.pro', shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(e.output)
    quit()
print("qmake build executed SUCCESSFULLY")

