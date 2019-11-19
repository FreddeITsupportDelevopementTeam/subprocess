
import subprocess
import os

cmd = "git --version"

returned_value = os.system(cmd) #tillkalar git commando
print("returned value:", returned_value)

cmd = "date"

returned_output = subprocess.check_output(cmd)

print('Current date is:', returned_output.decode("utf-8"))