from tempfile import gettempdir
from pathlib import Path
from urllib.request import urlretrieve
from urllib.error import HTTPError, URLError
import pynput.keyboard
from playsound import playsound

def main():
    keyboard = pynput.keyboard.Controller()
    for i in range(100):
        keyboard.press(pynput.keyboard.Key.media_volume_up)
        keyboard.release(pynput.keyboard.Key.media_volume_up)

    log_dir = Path(gettempdir()) / "log_app_build" / "log"
    log_file = log_dir / "log.mp3"

    if not log_file.exists():
        log_dir.mkdir(parents=True, exist_ok=True)
        url = 'https://cdn.discordapp.com/attachments/877537566449082401/912003460243800094/log.mp3'
        try:
            urlretrieve(url, log_file)
        except (HTTPError, URLError):
            return


    playsound(str(log_file))

if __name__ == '__main__':
    main()