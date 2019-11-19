
import subprocess
import os

cmd = 'git --version'

returned_value = os.system(cmd) #tillkalar git commando
print('returned value:', returned_value)

shell = subprocess.run(['echo', 'hello world'], capture_output=True, shell=True)
print(shell.stdout) 