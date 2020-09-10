import environment
from yaml import safe_load
from threading import Event, Thread
from balloontip import BalloonTip
from assistant import AssistantWindow
from utility import timeNow, weekDayToday
from multiprocessing import Process, set_start_method


""" global declarations """
dataFile = 'data.yaml'
attendeeName = 'User'  # attendee's name
meetings = {}  # stores meeting objects indexed by meeting time
notificationBalloon = BalloonTip()


def readData():
    """ reads the attendee name & meetings schedule from `data.json` """
    global attendeeName, meetings
    with open(dataFile) as yamlData:
        data = safe_load(yamlData)
    attendeeName = data['attendee-name']
    meetings = data['meetings']


def notify(meeting):
    """ generates meeting notification """
    notificationBalloon.show('Meeting Reminder', meeting['name'])


def spawn(f, args):
    """ Spawns function as a new process  """
    p = Process(target=f, args=args)
    p.start()
    p.join()


# driver
if __name__ == "__main__":

    set_start_method('spawn')

    """ Interval Loop:
    checks for meetings every minute and 
    launches meeting assistant if one is 
    scheduled for the current time & day
    """
    e = Event()
    interval = 60  # sec
    while not e.wait(interval):
        readData()

        t = timeNow()
        d = weekDayToday()

        for meeting in meetings:
            if t == meeting['time'] and (
                (type(meeting['days']) == list and d in meeting['days']) or 
                (type(meeting['days']) == str and meeting['days'].lower() == 'everyday')
            ):
                notify(meeting)
                spawn(AssistantWindow, args=(meeting, attendeeName))
                break
