import subprocess
import os

class MoveFile:
    def __init__(self,path,directory):
        self.path = path
        self.destination = destination

    def find_path(self):
        files = []

        for file in os.listdir(self.path):
            if file.endswith((".py",'.md','.png')):
                files.append(os.path.join(self.path,file))
        return files
    def move(self,files):
        for file in files:
            if file != "main.py":
                subprocess.check_call(["mv", file, self.destination])

if __name__ == "__main__":
    source_path = os.getcwd()
    destination = "/Users/tntirand/Desktop/mydocs/general/"

    mover = MoveFile(source_path,destination)

    files = mover.find_path()
    mover.move(files)