from pynput.keyboard import Key,Controller
from gtts import gTTS 
import os.path
from random import randint
import os
from playsound import playsound

def main():
    keyboard = Controller()
    for i in range(100):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)

    data = {}
    data['text'] = []
    data['text'].append({
        '1': 'I dont like cats',
        '2': 'eating a tree',
        '3': 'you are a dog?',
        '4': 'Minecraft',
        '5': '1 2 3 4',
        '6': 'lgbt',
        '7': 'bread',
        '8': 'nice',
        '9': 'drugs?',
        '10': 'you are listening me?',
        '11': 'who you are',
        '12': 'russia',
        '13': 'error 404',
        '14': 'dll file is missing',
        '15': 'a cow are flying',
        '16': 'im not beauty',
        '17': 'peanuts',
        '18': 'i eat 32kg of food per day',
        '19': 'Tripaloski',
        '20': 'Dead',
        '21': 'kill',
        '22': 'life is sad',
        '23': 'god are see you',
        '24': 'raining a lot',
        '25': 'go to the swimming pool',
        '26': 'is that a supra',
        '27': 'try linux',
        '28': 'im not poor',
        '29': '90 degrees',
        '30': 'win'
    })

    rand = randint(1,30)

    msg = data['text'][0][f'{rand}']

    tts = gTTS(msg, lang='en')
    tts.save("./voice.mp3")

    playsound('voice.mp3')

    os.remove("./voice.mp3")