import csv
from os import path
from utility import dateToday, weekDayToday, timeNow


def init():
    with open('meetings-log.csv', 'w', newline='') as csvfile:
        log = csv.writer(csvfile, delimiter=',')
        log.writerow(['Date', 'Day', 'Time', 'Subject/Topic', 'Attendance'])


def log(meetingName, attendance):
    if not path.isfile('meetings-log.csv'):
        init()
    with open('meetings-log.csv', 'a', newline='') as csvfile:
        log = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        log.writerow([
            dateToday(), weekDayToday(), timeNow(), meetingName, attendance
        ])
