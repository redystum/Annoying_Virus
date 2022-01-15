from keyboard import is_pressed
from pyperclip import copy
from time import sleep
import os.path
from tempfile import gettempdir
from json import load, dump
from random import randint

def json_create():

    temp = gettempdir()
    
    exist = os.path.exists(f"{temp}/log_app_build/log/log.json")
    if exist == True: return

    f = open(f"{temp}/log_app_build/log/log.json", "x")
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
    dump(data, f, indent=4)
    f.close()



def main():

    json_create()
    
    temp = gettempdir()

    f = open(f"{temp}/log_app_build/log/log.json", "r")

    data = load(f)

    f.close()
        
    rand = randint(1,30)

    msg = data['text'][0][f'{rand}']

    if is_pressed('ctrl') and is_pressed('c'):
        sleep(.5)
        copy(msg)

