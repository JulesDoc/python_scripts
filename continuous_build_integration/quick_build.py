import subprocess
import os
import configparser
import utils_module
from time import sleep

# Setting the config python parser
config = configparser.ConfigParser()
if not (os.path.isfile('config.ini')):
    print("No config file found!...quit")
    exit()
config.read('config.ini')
print("Config file read successfully...")
sleep(0.5)  # Time in seconds.

# System call for executing the script that copies 3rdparty libs
try:
    subprocess.run('python copy_3rd_party.py', shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(e.output)
    quit()

# Setting up files system folders and executing devenv. Debug || Release
# System calls are done by means of subprocess module
try:
    if config['DEFAULT']['debugOrRelease'] == 'debug':
        print("Executing devenv command, this operation will take a few minutes...")
        sleep(0.5)  # Time in seconds.
        debug = '"debug"'
        with open("outfile.txt", "wb", 0) as out:
            subprocess.run('devenv ' + config['PATHS']['terraSysBuildDir'] + '\\' + 'terrasys.sln /build '
                           + debug, shell=True, check=True, stdout=out)
        if config['DEFAULT']['buildWithCopyHeadersAndLibsToM'] == 'yes':
            subprocess.run('python copy_headers_to_m_drive.py', shell=True, check=True)
            subprocess.run('python copy_libs_to_m_drive.py', shell=True, check=True)

    elif config['DEFAULT']['debugOrRelease'] == 'release':
        print("Executing devenv command, this operation will take a few minutes...")
        sleep(0.5)  # Time in seconds.
        release = '"release"'
        with open("outfile.txt", "wb", 0) as out:
            subprocess.run('devenv ' + config['PATHS']['terraSysBuildDir'] + '\\' + 'terrasys.sln /build '
                           + release, shell=True, check=True, stdout=out)
        if config['DEFAULT']['buildWithCopyHeadersAndLibsToM'] == 'yes':
            subprocess.run('python copy_libs_to_m_drive.py', shell=True, check=True)
    else:
        print('Wrong config.ini file...quit')
except subprocess.CalledProcessError as e:
    print(e.stderr)
    utils_module.get_error_lines()
    quit()

# Sending email with information about the build
utils_module.get_error_lines()
print("Quick build executed successfully...")




