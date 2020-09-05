#!/usr/bin/env python3

import os
import notify2
from json import load
from sched import scheduler
from time import time, sleep
from utility import timeNow, copyToClipboard

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.environ.setdefault('DISPLAY', ':0')
os.environ.setdefault('XAUTHORITY', '/run/user/1000/gdm/Xauthority')
os.environ.setdefault('DBUS_SESSION_BUS_ADDRESS',
                      'unix:path=/run/user/1000/bus')

myName = ''
meetingURLBase = ''
meetings = {}

def readMeetingsData():
    with open('data.json') as jsonData:
        data = load(jsonData)
    global myName, meetings
    myName = data['myName']
    meetings = data['meetings']


def notify(meeting):
    notify2.init('Meetings Assistant')
    notify2.Notification(
      'Off to the meeting!', meeting['name']
    ).show()


# mainloop: 
# checks for meetings every minute
# launches if one scheduled
p = 1  # priority
interval = 60 #sec
sch = scheduler(time, sleep)
def mainloop(s):
    readMeetingsData()
    t = timeNow()
    if t in meetings.keys():
        launch()
    sch.enter(interval, p, mainloop, (s,))


sch.enter(interval, p, mainloop, (sch,))
# sch.run()