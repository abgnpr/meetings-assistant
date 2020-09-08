#!/usr/bin/env python3

from notify2 import init, Notification
import environment
from yaml import safe_load
from threading import Event
from assistant import AssistantWindow
from utility import timeNow, weekDayToday
from multiprocessing import Process, set_start_method


""" global declarations """
dataFile = 'data.yaml'
attendeeName = 'User'  # attendee's name
meetings = {}  # stores meeting objects indexed by meeting time


def readData():
    """ reads the attendee name & meetings schedule from `data.json` """
    global attendeeName, meetings
    with open(dataFile) as yamlData:
        data = safe_load(yamlData)
    attendeeName = data['attendee-name']
    meetings = data['meetings']


def notify(meeting):
    """ generates meeting notification """
    init('Meetings Assistant')
    Notification(
        summary='Meeting Reminder', 
        message=meeting['name']
    ).show()


# driver
if __name__ == "__main__":

    set_start_method('fork')
    # this is a unix exclusive multiprocessing start method.
    # Make AssistantWindow work with set_start_method('spawn')
    # to enable platform independance.

    """ Interval Loop:
    checks for meetings every minute and 
    launches meeting assistant if one is 
    scheduled for the current time & day
    """
    e = Event()
    interval = 60  # sec
    while not e.wait(interval):

        # read data.json
        readData()

        t = timeNow()
        d = weekDayToday()

        for meeting in meetings:
            if t == meeting['time'] and (
                (
                    type(meeting['days']) == list
                    and d in meeting['days']
                ) or (
                    type(meeting['days']) == str
                    and meeting['days'].lower() == 'everyday'
                )
            ):
                # notify about the meeting
                notify(meeting)

                # start AssistantWindow as a new process
                aw = Process(
                    target=AssistantWindow,
                    args=(meeting, attendeeName)
                )
                aw.start()
                aw.join()  # wait for assistant window to terminate

                break
