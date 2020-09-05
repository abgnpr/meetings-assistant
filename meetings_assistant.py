#!/usr/bin/env python3

import os
import notify2
from json import load
from sched import scheduler
from time import time, sleep
from webbrowser import open_new
from logger_prompt import showLoggerPrompt
from utility import timeNow, copyToClipboard

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.environ.setdefault('DISPLAY', ':0')
os.environ.setdefault('XAUTHORITY', '/run/user/1000/gdm/Xauthority')
os.environ.setdefault('DBUS_SESSION_BUS_ADDRESS',
                      'unix:path=/run/user/1000/bus')

# globals
myName = ''
meetingURLBase = ''
meetings = {}
pswdPromptDelay = 0


def readData():
    with open('data.json') as jsonData:
        data = load(jsonData)
    global myName, meetingURLBase, meetings, pswdPromptDelay
    myName = data['myName']
    meetingURLBase = data['meetingURLBase']
    meetings = data['meetings']
    pswdPromptDelay = data['pswdPromptDelay']


def launch(t):
    notify2.init('Meetings Assistant')
    notify2.Notification('Off to the meeting!', meetings[t]['name']).show()
    open_new(meetingURLBase + meetings[t]['id'])
    copyToClipboard(myName)
    sleep(pswdPromptDelay)
    copyToClipboard(meetings[t]['pswd'])
    sleep(60)
    showLoggerPrompt(meetings[t]['name'])


sch = scheduler(time, sleep)
interval = 60  # sec
p = 1  # priority

# loop to check for meetings every minute
def loop(s):
    readData()
    t = timeNow()
    if t in meetings.keys():
        launch(t)
    sch.enter(interval, p, loop, (s,))


def main():
    sch.enter(interval, p, loop, (sch,))
    sch.run()


# main()
readData()
launch('09:00')
