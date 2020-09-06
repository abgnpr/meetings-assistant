#!/usr/bin/env python3

import environment
from json import load
from sched import scheduler
from time import time, sleep
from utility import timeNow, notify
from assistant import AssistantWindow


""" global declarations """
attendeeName = 'User'  # attendee's name
meetings = {}  # stores meeting objects indexed by meeting time
dataFile = 'data.json'


def readData():
    """ reads the attendee name & meetings schedule from `data.json` """
    global attendeeName, meetings
    with open(dataFile) as jsonData:
        data = load(jsonData)
    attendeeName = data['attendee-name']
    meetings = data['meetings']


# un-comment to test a sample meeting
# dataFile = 'sampledata.json'
# readData()
# notify(meetings['09:00'])
# AssistantWindow(meeting=meetings['09:00'], attendeeName=attendeeName).show()
# exit()


""" mainloop configuration """
p = 1  # priority
interval = 60  # sec
sch = scheduler(time, sleep)  # init scheduler


def mainloop(s):
    """
    checks for meetings every minute and 
    launches meeting assistant if one is 
    scheduled for the current time
    """
    readData()
    t = timeNow()
    if t in meetings.keys():
        notify(meetings[t])
        AssistantWindow(meeting=meetings[t], attendeeName=attendeeName).show()
    sch.enter(interval, p, mainloop, (s,))


""" start mainloop() """
sch.enter(interval, p, mainloop, (sch,))
sch.run()
