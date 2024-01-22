import subprocess

def git_save():
    try:
        subprocess.check_call(["git", "add", "."])
        subprocess.check_call(["git", "commit", "-m", "save the changes"])
        subprocess.check_call(["git", "push"])
        print("pushed successfully successful.")
    except subprocess.CalledProcessError as e:
        print(f"Action failed. Error: {e}")

git_save()




