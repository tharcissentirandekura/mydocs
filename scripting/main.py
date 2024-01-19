import subprocess
import os
from time import sleep

def search(path):
    paths = []
    for root,dirs,files in os.walk(path):
        for file in files:
            abs_path = os.path.join(root,file)
            paths.append(abs_path)
    return paths
           
def run(root):
    path = search(root)
    for i in range(len(path)):
        if path[i].split('/')[-1] != "main.py" and path[i].split('/')[-1].endswith(".py"):
            #run the files in the directory
            subprocess.run(['python3',path[i]])
            print(f"Successfully executed __{path[i].split('/')[-1]}__")
            sleep(2)

if __name__ == "__main__":
    path = os.getcwd()
    run(path)

