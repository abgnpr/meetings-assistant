#!/usr/bin/env python3

from json import load
import environment
from threading import Event
from assistant import AssistantWindow
from utility import timeNow, weekDayToday, notify
from multiprocessing import Process, set_start_method


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


# driver
if __name__ == "__main__":

    set_start_method('fork')
    # this is a unix exclusive multiprocessing start method.
    # Make AssistantWindow work with set_start_method('spawn')
    # to enable platform independance.

    """ Interval Loop:
    checks for meetings every minute and 
    launches meeting assistant if one is 
    scheduled for the current time
    """
    e = Event()
    interval = 60  # sec
    while not e.wait(interval):
        
        # read data.json
        readData()
        
        t = timeNow()
        if t in meetings.keys() and (
            weekDayToday() in meetings[t]['days']
            or meetings[t]['days'].lower() == 'everyday'
        ):
            
            # notify about the meeting
            notify(meetings[t])
            
            # start AssistantWindow as a new process
            aw = Process(
                target=AssistantWindow,
                args=(meetings[t], attendeeName)
            )
            aw.start()
            aw.join()  # wait for assistant window to terminate
