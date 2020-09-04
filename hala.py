#!/usr/bin/env python3

import os
from time import time, sleep
from sched import scheduler
from datetime import datetime
from json import load
from subprocess import Popen, PIPE, DEVNULL
import notify2

os.chdir(os.path.dirname(os.path.realpath(__file__)))

myName = ''
meetingURLBase = ''
meetings = {}
pswdPromptDelay = 0

os.environ.setdefault('DISPLAY', ':0')
os.environ.setdefault('XAUTHORITY', '/run/user/1000/gdm/Xauthority')
os.environ.setdefault('DBUS_SESSION_BUS_ADDRESS',
                      'unix:path=/run/user/1000/bus')


def timeNow():
    h = datetime.now().hour
    m = datetime.now().minute
    h = str(h) if h > 9 else '0' + str(h)
    m = str(m) if m > 9 else '0' + str(m)
    return h + ':' + m


def readData():
    with open('data.json') as jsonData:
        data = load(jsonData)
    global myName, meetingURLBase, meetings, pswdPromptDelay
    myName = data['myName']
    meetingURLBase = data['meetingURLBase']
    meetings = data['meetings']
    pswdPromptDelay = data['pswdPromptDelay']


def launch(meetingURL):
    Popen(['xdg-open', meetingURL], stdout=DEVNULL, stderr=DEVNULL)


def terminal(): # todo - prompt
    Popen(['gnome-terminal', '--', './hi.py'])


def copyToClipboard(text):
    echo = Popen(['echo', text], stdout=PIPE)
    Popen(['xclip', '-sel', 'clip'], stdin=echo.stdout)


sch = scheduler(time, sleep)
interval = 60  # sec
p = 1  # priority


def loop(s):
    readData()
    t = timeNow()
    if t in meetings.keys():
        launch(meetingURLBase + meetings[t]['id'])
        notify2.init('Meetings Assistant')
        notify2.Notification('Off to the meeting!', 'Haha').show()
        copyToClipboard(myName)
        sleep(pswdPromptDelay)
        copyToClipboard(meetings[t]['pswd'])

    sch.enter(interval, p, loop, (s,))


sch.enter(interval, p, loop, (sch,))
sch.run()
