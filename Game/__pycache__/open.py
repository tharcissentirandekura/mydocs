import subprocess
import os

path = os.listdir()[1]
print(path)

# subprocess.check_call(["uncompyle6",path,">","decomiled.py"])