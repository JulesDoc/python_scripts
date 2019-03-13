import configparser
import os
from shutil import rmtree
import subprocess
from time import sleep

config = configparser.ConfigParser()
if not (os.path.isfile('config.ini')):
    print('No config file found!...quit')
    exit()
config.read('config.ini')
print("Config file read successfully...")
sleep(0.5)  # Time in seconds.

if os.path.isdir(config['PATHS']['qtDeployDir']):
    try:
        rmtree(config['PATHS']['qtDeployDir'])
    except IOError:
        print("Problem removing include folder. Removing header folder manually")
        try:
            subprocess.run('rd /S /Q ' + config['PATHS']['qtDeployDir'], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(e.output)
            quit()

# Debug
os.makedirs(config['PATHS']['qtDeployDebugDir'])

try:
    print("Executing windeployqt debug command...")
    sleep(0.5)  # Time in seconds.
    return_value = subprocess.run(['windeployqt', config['PATHS']['executablePath'], '--debug', '--no-translations',
                                   '--no-plugins', '--dir', config['PATHS']['qtDeployDebugDir']], shell=True,
                                  check=True)
except subprocess.CalledProcessError as e:
    print(e.output)
    quit()

os.mkdir(config['PATHS']['qtDeployDebugDir'] + '\\' + 'plugins')
try:
    print("Executing windeployqt debug command in plugins...")
    sleep(0.5)  # Time in seconds.
    return_value = subprocess.run(['windeployqt', config['PATHS']['executablePath'], '--debug', '--no-translations',
                                   '--no-libraries', '--no-compiler-runtime', '--dir',
                                   config['PATHS']['qtDeployDebugDir'] + '\\' + 'plugins'], shell=True,
                                  check=True)
except subprocess.CalledProcessError as e:
    print(e.output)
    quit()

# Release
os.makedirs(config['PATHS']['qtDeployReleaseDir'])
# os.mkdir(config['PATHS']['qtDeployReleaseDir'])
try:
    print("Executing windeployqt release command...")
    sleep(0.5)  # Time in seconds.
    return_value = subprocess.run(['windeployqt', config['PATHS']['executablePath'], '--release', '--no-translations',
                                   '--no-plugins', '--dir', config['PATHS']['qtDeployReleaseDir']], shell=True,
                                  check=True)
except subprocess.CalledProcessError as e:
    print(e.output)
    quit()

os.mkdir(config['PATHS']['qtDeployReleaseDir'] + '\\' + 'plugins')
try:
    print("Executing windeployqt release command in plugins...")
    sleep(0.5)  # Time in seconds.
    return_value = subprocess.run(['windeployqt', config['PATHS']['executablePath'], '--release', '--no-translations',
                                   '--no-libraries', '--no-compiler-runtime', '--dir',
                                   config['PATHS']['qtDeployReleaseDir'] + '\\' + 'plugins'], shell=True,
                                  check=True)
except subprocess.CalledProcessError as e:
    print(e.output)
    quit()
print('windeployqt command successfully executed')

