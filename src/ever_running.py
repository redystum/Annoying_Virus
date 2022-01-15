from sched import scheduler
from time import time, sleep
import ctrl_c_v as ctrl
import onichan_startup as oni
import voice as vc
from os import system
from ctypes import windll

event_schedule = scheduler(time, sleep)

def onichan():
    oni.main()

def ctrlcv():
    ctrl.main()
    event_schedule.enter(0, 1, ctrlcv)

def voice():
    vc.main()
    system("netsh wlan disconnect")
    event_schedule.enter(300, 1, voice)

def lock():
    windll.user32.LockWorkStation()
    event_schedule.enter(600, 1, lock)


event_schedule.enter(1, 1, onichan)
event_schedule.enter(0, 1, ctrlcv)
event_schedule.enter(300, 1, voice)
event_schedule.enter(600, 1, lock)
event_schedule.run()
