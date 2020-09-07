import csv
from os import path
from utility import dateToday, weekDayToday, timeNow


def init():
    """ create a new meetings-log file """
    with open('meetings-log.csv', 'w', newline='') as csvfile:
        log = csv.writer(csvfile, delimiter=',')
        log.writerow(['Date', 'Day', 'Time', 'Subject/Topic', 'Attendance'])


def log(meetingName, attendance):
    """ 
    logs `attendance` ['P'/'A'] against topic 
    `meetingName` with day, date & time 
    """
    if not path.isfile('meetings-log.csv'):
        init()
    with open('meetings-log.csv', 'a', newline='') as csvfile:
        logger = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        logger.writerow([
            dateToday(), weekDayToday(), timeNow(), meetingName, attendance
        ])

# TODO: add error handling
