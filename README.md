# Annoying_Virus
A "virus" just to make fun of your friend, it's just annoying, it won't damage or steal anything!

# How it works
when the file is executed it will be copied into the windows startup folder. (it runs as soon as it is ejected) \
Once in the startup folder when the pc is turned on the virus will run.

# What he does
### When the PC is turned on
* The virus will turn the pc volume to maximum and play "onii chan".

### Always running
* The classic Ctrl C, Ctrl V will not work, the virus will paste a random phrase

### 5 in 5 minutes
* The google voice will say a random phrase with the pc sound at maximum
* Wifi is disconnected, not turned off, just disconnected, to give a slight lag in games and apps

### 10 in 10 minutes
* The coputer will go to the lock screen, making you have to log in again

# How to stop / remove
Go to the task manager \
`WIN R` `taskmgr` \
finish the System_StartUp_Apps.exe task \
`Right button` `End task` \
Remove System_StartUp_Apps.exe from the windows startup folder \
`WIN R` `shell:startup` `delete the file` 

* The file System_StartUp_Apps.exe is not really part of the system, it just has that name so you can't delete it and get rid of the virus

# Pyinstaller
```
pyinstaller --noconfirm --onefile --windowed -i NONE --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse._win32 main.py
```
