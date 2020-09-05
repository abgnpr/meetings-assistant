#!/usr/bin/env python3

import notify2
import environment
from json import load
from sched import scheduler
from utility import timeNow
from time import time, sleep
from assistant import AssistantWindow


""" global declarations """

# Attendee's name
attendeeName = 'User'

# stores meeting objects  indexed by meeting time
meetings = {} 


def readMeetingsData():
    """ reads the meeting schedule from `data.json` """
    global attendeeName, meetings
    with open('data.json') as jsonData:
        data = load(jsonData)
    attendeeName = data['attendee-name']
    meetings = data['meetings']


def notify(meeting):
    """ generates meeting notification """
    notify2.init('Meetings Assistant')
    notify2.Notification(
        'Meeting Reminder', meeting['name']
    ).show()


# test
readMeetingsData()
notify(meetings['09:00'])
AssistantWindow(meeting=meetings['09:00'], attendeeName=attendeeName).show()
exit()


""" mainloop configuration """
p = 1  # priority
interval = 60  # sec
sch = scheduler(time, sleep) # init scheduler


def mainloop(s):
    """
    checks for meetings every minute and 
    launches meeting assistant if one is 
    scheduled for current time
    """
    readMeetingsData()
    t = timeNow()
    if t in meetings.keys():
        notify(meetings[t])
        AssistantWindow(meeting=meetings[t], attendeeName=attendeeName).show()
    sch.enter(interval, p, mainloop, (s,))


""" start mainloop() """
sch.enter(interval, p, mainloop, (sch,))
# sch.run()
